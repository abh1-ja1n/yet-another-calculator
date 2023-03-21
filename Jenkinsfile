pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build and Test Frontend') {
      steps {
        dir(path: 'sci-calc') {
          sh 'npm install'
          // sh 'npm run test'
          sh 'npm run build'
        }
      }
    }

    stage('Build and Test Backend') {
      steps {
        dir(path: 'sci-calc-backend') {
          sh 'pwd' 
          sh 'pip3 install -r requirements.txt'
          sh 'python3 app.py &'
          sh 'python3 -m unittest discover tests'
        }
      }
    }

    stage('Containerize Frontend') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'a1e5a121-5455-410f-9e53-c0af6a006fde', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          dir(path: 'sci-calc') {
            sh 'docker build -t $USERNAME/sci-calc-frontend-image .'
            sh 'docker login -u $USERNAME -p $PASSWORD'
            sh 'docker push $USERNAME/sci-calc-frontend-image'
          }
        }
      }
    }

    stage('Containerize Backend') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'a1e5a121-5455-410f-9e53-c0af6a006fde', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          dir(path: 'sci-calc-backend') {
            sh 'docker build -t $USERNAME/sci-calc-backend-image .'
            sh 'docker login -u $USERNAME -p $PASSWORD'
            sh 'docker push $USERNAME/sci-calc-backend-image'
          }
        }
      }
    }

    
    stage('Deploy') {
  steps {
    sh 'ansible-playbook -i inventory deploy.yaml --extra-vars "@vars.yml" '
  }
}

  }
}
