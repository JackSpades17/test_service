pipeline {
    agent any
    
    stages { 
        stage('Check') {
            steps { 
                sh 'ansible --version'
            }
        }
        stage('Checkout') {
            steps {
                git branch: 'master', url: "git@github.com:JackSpades17/jenkins.git",  credentialsId: 'github_key'
            }
        }
        stage('Deploy') {
            steps {
                sh 'ansible-playbook -i hosts.ini main.yml -t deploy'
            }
        }
    }
}