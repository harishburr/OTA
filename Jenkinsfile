pipeline {
    agent any

    stages {
        stage('OTA-Update-trigger') {
            steps {
                script {
                    echo 'Triggering OTA update...'
                    // Add steps to trigger OTA update
                }
            }
            post {
                success {
                    build job: 'Moving-Binary-Into-Target-hosts', wait: false
                }
            }
        }

        stage('Moving-Binary-Into-Target-hosts') {
            steps {
                script {
                    echo 'Moving binary to target hosts...'
                    // Add steps to move binary to target hosts
                }
            }
            post {
                success {
                    build job: 'Build-Binary-in-Target-Host', wait: false
                }
            }
        }

        stage('Build-Binary-in-Target-Host') {
            steps {
                script {
                    echo 'Building binary in target hosts...'
                    // Add steps to build binary in target hosts
                }
            }
            post {
                success {
                    build job: 'OTA-Deployament-Edge-device', wait: false
                }
            }
        }

        stage('OTA-Deployament-Edge-device') {
            steps {
                echo 'Deploying OTA update to edge devices...'
                // Add steps to deploy OTA update to edge devices
            }
            post {
                success {
                    echo 'Starting SSH commands...'
                    executeSSHCommands()
                }
            }
        }
    }
}

def executeSSHCommands() {
    // Define vehicles and execute SSH commands in parallel
    def vehicles = [
        'Toyota_Land_Cruiser_1',
        'Toyota_Fortuner_2',
        'Toyota_Glanza_3',
        'Toyota_Hilux_4',
        'Toyota_Camry_5',
        'TOYOTA_Vellfire_6',
        'Toyota_Corolla_7',
        'TOYOTA_RUSH_8',
        'Toyota_Tacoma_9',
        'Toyota_Yaris_10'
    ]

    // Execute SSH commands in parallel
    def stepsForParallel = [:]
    vehicles.each { vehicle ->
        stepsForParallel["${vehicle}"] = {
            script {
                echo "Executing SSH command for ${vehicle}..."
                sh "ssh -t ubuntu@54.193.137.189 'docker logs ${vehicle}'"
                echo "Environment health check done for ${vehicle}."
            }
        }
    }

    parallel stepsForParallel
}
