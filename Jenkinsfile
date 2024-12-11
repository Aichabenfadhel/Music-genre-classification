pipeline {
    agent any

    stages {
        stage('Checkout Code and repository') {
            steps {
                echo 'Checking out repository...'
                git branch: 'master', url: 'https://github.com/Aichabenfadhel/Music-genre-classification.git'
            }
        }

        stage('Build and Start Services with Docker Compose') {
            steps {
                script {
                    
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
                    
                    if (isUnix()) {
                        sh '''
                            docker-compose exec vgg-backend pytest /app/Backend/vgg_service/Tests
                            docker-compose exec svm-backend pytest /app/Backend/svm_service/Tests

                        '''
                    } else {
                        bat '''
                            REM Run tests in vgg-backend container
                            docker-compose exec vgg-backend pytest C:/Users/user/Desktop/3eme année Ensit/ML/Music_classification_Mini_projet/Backend/vgg_service/Tests
                            REM Run tests in svm-backend container
                            docker-compose exec svm-backend pytest C:/Users/user/Desktop/3eme année Ensit/ML/Music_classification_Mini_projet/Backend/svm_service/Tests
                        '''
                    }
                }
            }
        }

        

        stage('Push Docker Images') {
            steps {
                script {
                    
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
}