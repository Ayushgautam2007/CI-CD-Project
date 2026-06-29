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
        sh '''
            echo "===== DEBUG ====="
            env | grep MONGO

            echo "First 20 characters:"
            printf "%s\n" "$MONGO_URI" | head -c 20
            echo
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
