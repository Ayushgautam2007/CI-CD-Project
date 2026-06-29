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
        emailext(
            subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """
Build Successful

Job: ${env.JOB_NAME}

Build Number: ${env.BUILD_NUMBER}

Build URL:
${env.BUILD_URL}
""",
            to: "ayush.gautam071997@gmail.com"
        )
    }

    failure {
        emailext(
            subject: "FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """
Build Failed

Job: ${env.JOB_NAME}

Build Number: ${env.BUILD_NUMBER}

Build URL:
${env.BUILD_URL}
""",
            to: "ayush.gautam071997@gmail.com"
        )
    }

    always {
        echo "Pipeline execution finished."
    }
}
