pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/harishburr/OTA.git'
            }
        }
        stage('Copy Simulator Script') {
            steps {
                sh 'cp simulator.py /home/ubuntu/OTA/OTA_Log'
            }
        }
        stage('Build Docker Image') {
            steps {
                dir('/home/ubuntu/OTA/OTA_Log') {
                    sh 'docker build -t ota_v1 .'
                }
            }
        }
        stage('Start OTA Log Analysis Services') {
            steps {
                dir('/home/ubuntu/OTA/OTA_Log_analysis') {
                    sh 'docker-compose up -d'
                }
            }
        }
        stage('Start OTA Services') {
            steps {
                dir('/home/ubuntu') {
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
