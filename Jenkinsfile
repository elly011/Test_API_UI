pipeline {
    agent any

    environment {
        REPORT_DIR = "reports"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/elly011/Test_API_UI.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                pip install --upgrade pip
                if exist requirements.txt pip install -r requirements.txt
                npm install -g newman
                '''
            }
        }

        stage('Run UI Tests (Selenium)') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                pytest test_automa_UI\\*.py --alluredir=%REPORT_DIR%\\allure-results
                '''
            }
        }

        stage('Run API Tests (Postman)') {
            steps {
                bat '''
                newman run "newman API\\postman_collection.json" ^
                -e "newman API\\newman_env.json" ^
                --reporters cli,allure --reporter-allure-export %REPORT_DIR%\\allure-results
                '''
            }
        }
    }

    post {
        always {
            echo "🔹 Génération du rapport Allure même si les tests ont échoué..."
            bat '''
            allure generate %REPORT_DIR%\\allure-results --clean -o %REPORT_DIR%\\allure-report
            '''
            publishHTML([
                reportDir: "%REPORT_DIR%\\allure-report",
                reportFiles: 'index.html',
                reportName: 'Allure Test Report'
            ])
        }
        success {
            echo "✅ Build et tests réussis ! Rapport disponible dans Jenkins."
        }
        failure {
            echo "❌ Les tests ont échoué. Consulte le rapport Allure pour plus de détails."
        }
    }
}
