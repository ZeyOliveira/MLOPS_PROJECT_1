pipeline {
    agent any

    environment{
        VENV_DIR = 'venv'
    }

    stages {
        stage('Cloning Github repo to Jenkins') {
            steps { 
                echo 'Cloning Github repo to Jenkins.............' 
                
                checkout scmGit(
                    branches: [[name: '*/main']], 
                    extensions: [],
                    userRemoteConfigs: [[
                        credentialsId: 'github-token',
                        url: 'https://github.com/ZeyOliveira/MLOPS_PROJECT_1.git' 
                    ]]
                )
            }
        }


        stage('Setting up our Virtual Environment and Installing Dependencies') {
            steps { 
                echo 'Setting up our Virtual Environment and Installing Dependencies.............'
                sh '''
                python -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -e .
                ''' 
            }
        }
    }
}