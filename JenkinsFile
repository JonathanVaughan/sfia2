pipeline{
    agent any
    stages{
        stage("Executable Scripts"){
            steps{
                sh 'chmod +x ./scripts/*'
            }
        }
        stage("Export Variables"){
            steps{
                sh './scripts/envi.sh'
            }
        }
        stage("Install Ansible and Run Playbook"){
            steps{
                sh './scripts/ansible.sh'
            }
        }
        stage("Deploy Stack"){
            steps{
                sh './scripts/docker.sh'
            }
        }
    }
}