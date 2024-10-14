pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('my-image')
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.image('my-image').inside {
                        sh 'python -m py_compile main.py'
                    }
                }
            }
        }
    }
}
