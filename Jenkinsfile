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

    // stage('Containerize') {
    //   steps {
    //     dir(path: 'sci-calc') {
    //       sh 'docker build -t sci-calc-frontend-image .'
    //     }

    //     dir(path: 'sci-calc-backend') {
    //       sh 'docker build -t sci-calc-backend-image .'
    //     }
    //   }
    // }

    stage('Containerize Frontend') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
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
        withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          dir(path: 'sci-calc-backend') {
            sh 'docker build -t $USERNAME/sci-calc-backend-image .'
            sh 'docker login -u $USERNAME -p $PASSWORD'
            sh 'docker push $USERNAME/sci-calc-backend-image'
          }
        }
      }
    }
  }
}
