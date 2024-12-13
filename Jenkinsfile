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
                            
                            pytest Backend/vgg_service/Tests
                            pytest Backend/svm_service/Tests

                        '''
                    } else {
                        """
                            pytest Backend\\vgg_service\\Tests
                            pytest Backend\\svm_service\\Tests
                        """
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