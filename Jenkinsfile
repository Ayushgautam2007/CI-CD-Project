pipeline {
    agent any

    environment {
        MONGO_URI = "mongodb+srv://db_user:eHospital%401234%23@cluster0.ur5ysem.mongodb.net/mydb?retryWrites=true&w=majority&appName=Cluster0"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'YOUR_GITHUB_REPO_URL'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Debug Environment') {
            steps {
                sh '''
                    echo "===== DEBUG ====="
                    echo "Workspace: $WORKSPACE"
                    env | grep MONGO || true

                    echo "Mongo URI preview:"
                    echo $MONGO_URI | cut -c1-20
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    pytest -v || exit 1
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask application...'
                sh '''
                    chmod +x start_flask.sh
                    nohup ./start_flask.sh > flask.log 2>&1 &
                    echo "Flask started in background"
                '''
            }
        }
    }

    post {

        success {
            echo 'Pipeline completed successfully!'

            emailext(
                to: 'ayush.gautam071997@gmail.com',
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
Hello Ayush,

Your Jenkins Pipeline has completed successfully.

Job Name : ${env.JOB_NAME}
Build No : ${env.BUILD_NUMBER}
Status   : SUCCESS

Workspace:
${env.WORKSPACE}

Build URL:
${env.BUILD_URL}

Regards,
Jenkins
"""
            )
        }

        failure {
            echo 'Pipeline failed!'

            emailext(
                to: 'ayush.gautam071997@gmail.com',
                subject: "FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
Hello Ayush,

Your Jenkins Pipeline has FAILED.

Job Name : ${env.JOB_NAME}
Build No : ${env.BUILD_NUMBER}
Status   : FAILED

Workspace:
${env.WORKSPACE}

Build URL:
${env.BUILD_URL}

Regards,
Jenkins
"""
            )
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
