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

    stage('Containerize') {
      steps {
        dir(path: 'sci-calc') {
          sh 'docker build -t sci-calc-frontend-image .'
        }

        dir(path: 'sci-calc-backend') {
          sh 'docker build -t sci-calc-backend-image .'
        }
      }
    }
  }
}
