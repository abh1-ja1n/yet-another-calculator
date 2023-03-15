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
                dir('sci-calc') {
                    sh 'npm install'
                    sh 'npm run test'
                    sh 'npm run build'
                }
            }
        }
        stage('Build and Test Backend') {
            steps {
                dir('sci-calc-backend') {
                    sh 'pip install -r requirements.txt'
                    sh 'python -m unittest discover tests'
                }
            }
        }
        // stage('Build Docker Image') {
        //     steps {
        //         sh 'docker build -t sci-calc-backend backend/.'
        //         sh 'docker build -t sci-calc-frontend frontend/.'
        //     }
        // }
    }
}
