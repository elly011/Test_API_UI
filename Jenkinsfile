pipeline {
    agent any

    environment {
        REPORT_DIR = "rapports"
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
                if exist exigences.txt pip install -r exigences.txt
                npm install -g newman
                '''
            }
        }

        stage('Run UI Tests (Selenium)') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                if exist test_automa_UI (
                    pytest test_automa_UI --alluredir=%REPORT_DIR%\\allure-results
                ) else (
                    echo "❌ Dossier test_automa_UI introuvable !"
                )
                '''
            }
        }

        stage('Run API Tests (Postman)') {
            steps {
                bat '''
                if exist "API Newman\\postman_collection.json" (
                    newman run "API Newman\\postman_collection.json" ^
                    -e "API Newman\\newman_env.json" ^
                    --reporters cli,allure --reporter-allure-export %REPORT_DIR%\\allure-results
                ) else (
                    echo "❌ Collection Postman introuvable !"
                )
                '''
            }
        }
    }

    post {
        always {
            echo "🔹 Génération du rapport Allure même si les tests ont échoué..."
            bat '''
            if exist %REPORT_DIR%\\allure-results (
                allure generate %REPORT_DIR%\\allure-results --clean -o %REPORT_DIR%\\allure-report
            ) else (
                echo "❌ Aucun résultat Allure à générer !"
            )
            '''
            publishHTML([
                reportDir: "%REPORT_DIR%\\allure-report",
                reportFiles: 'index.html',
                reportName: 'Allure Test Report'
            ])
            archiveArtifacts artifacts: 'rapports/allure-report/**', fingerprint: true
        }
        success {
            echo "✅ Build et tests réussis ! Rapport disponible dans Jenkins."
        }
        failure {
            echo "❌ Les tests ont échoué. Consulte le rapport Allure pour plus de détails."
        }
    }
}
