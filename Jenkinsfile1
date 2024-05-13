pipeline {
    agent any

    parameters {
        string(name: 'filePath', description: 'Path to the YAML file')
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                git 'https://github.com/alokrajad/first_jenkins_pipeline'
            }
        }
        stage('Replace x=5 with x=3') {
            steps {
                script {
                    def filePath = params.filePath

                    // Execute Python script to perform replacement
                    sh "python replace_values.py $filePath"
                }
            }
        }
    }
}