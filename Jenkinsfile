pipeline {
    agent any

    environment {
        MONGO_URI = credentials('mongo-uri')
    }

    stages {

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
                echo 'Checking MONGO_URI...'
                sh '''
                    if [ -z "$MONGO_URI" ]; then
                        echo "ERROR: MONGO_URI is NOT set!"
                        exit 1
                    fi

                    echo "MONGO_URI starts with:"
                    echo "$MONGO_URI" | cut -c1-30
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                    chmod +x start_flask.sh
                    ./start_flask.sh
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
