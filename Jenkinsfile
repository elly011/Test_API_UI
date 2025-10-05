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
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                npm install -g newman
                '''
            }
        }

        stage('Run UI Tests (Selenium)') {
            steps {
                sh '''
                source venv/bin/activate
                pytest tests/ui/test_ui_selenium.py --alluredir=${REPORT_DIR}/allure-results
                '''
            }
        }

        stage('Run API Tests (Postman)') {
            steps {
                sh '''
                newman run tests/api/postman_collection.json \
                -e tests/api/newman_env.json \
                --reporters cli,allure --reporter-allure-export ${REPORT_DIR}/allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                allure generate ${REPORT_DIR}/allure-results --clean -o ${REPORT_DIR}/allure-report
                '''
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    reportDir: "${REPORT_DIR}/allure-report",
                    reportFiles: 'index.html',
                    reportName: 'Allure Test Report'
                ])
            }
        }
    }

    post {
        success {
            echo "✅ Build et tests réussis ! Rapport disponible dans Jenkins."
        }
        failure {
            echo "❌ Les tests ont échoué. Consulte le rapport Allure pour plus de détails."
        }
    }
}
