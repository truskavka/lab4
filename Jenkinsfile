pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python -m py_compile main.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage('Deliver') { 
            steps {
                sh "pyinstaller --onefile main.py" 
            }
            post {
                success {
                    archiveArtifacts 'dist/main.exe' 
                }
            }
        }
    }
}
