pipeline {
    agent any

    environment {
        PYTHON = '/Users/apple/opt/anaconda3/bin/python'
    }
    parameters {
        string(name: 'filePath', description: 'Path to the YAML file')
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                checkout scm
            }
        }
        stage('Replace x=5 with x=3') {
            steps {
                sh "chmod +x replace_value.py"
                script {
                    def filePath = params.filePath

                    // Execute Python script to perform replacement
                    sh "${env.PYTHON} replace_values.py $filePath"
                }
            }
        }
    }
}