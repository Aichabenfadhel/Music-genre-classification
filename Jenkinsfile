pipeline {
    agent any

    stages {
        stage('Checkout Code and Repository') {
            steps {
                echo 'Checking out repository...'
                git branch: 'master', url: 'https://github.com/Aichabenfadhel/Music-genre-classification.git'
            }
        }

        stage('Build and Start Services with Docker Compose') {
            steps {
                script {
                    echo 'Building and starting services with Docker Compose...'
                    if (isUnix()) {
                        sh 'docker-compose -f docker-compose.yml up --build -d'
                    } else {
                        bat 'docker-compose -f docker-compose.yml up --build -d'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests...'

                        bat '''
                            REM Run tests in vgg-backend container
                            docker-compose exec vgg-backend pytest C:/path/to/your/project/Backend/vgg_service/Tests
                            REM Run tests in svm-backend container
                            docker-compose exec svm-backend pytest C:/path/to/your/project/Backend/svm_service/Tests
                        '''
                    }
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    echo 'Pushing Docker images...'
                    if (isUnix()) {
                        sh 'docker-compose push'
                    } else {
                        bat 'docker-compose push'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying app...'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker containers and images...'
            // Cleanup Docker containers and images if necessary
            if (isUnix()) {
                sh 'docker-compose down'
            } else {
                bat 'docker-compose down'
            }
        }
    }
}
