pipeline {
    agent any

    environment {
        PYTHON = "python3"
        PIP = "pip3"
    }

    stages {

        stage('Build') {
            steps {
                echo '========== Build Stage =========='
                sh '''
                    $PYTHON --version
                    $PIP --version

                    $PYTHON -m pip install --upgrade pip
                    $PIP install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo '========== Test Stage =========='
                sh '''
                    pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '========== Deploy Stage =========='
                sh '''
                    chmod +x start_flask.sh
                    ./start_flask.sh
                '''
            }
        }
    }

    post {

        success {
            echo '✅ Build, Test, and Deployment completed successfully.'
        }

        failure {
            echo '❌ Pipeline failed.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
