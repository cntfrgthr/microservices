pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        // Указываем Python и виртуальное окружение
        PYTHON_ENV = 'python3 -m venv venv'
        VENV_ACTIVATE = '. venv/bin/activate'
    }

    stages {
        stage('Checkout Project') {
            steps {
                // Клонирование исходного кода из основного репозитория
                checkout scm
            }
        }

        stage('Checkout Tests') {
            steps {
                // Клонирование репозитория с тестами
                dir('tests') {
                    git url: 'https://github.com/dshumeiko/test.git', branch: 'main'
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Установка виртуального окружения и зависимостей
                sh "${env.PYTHON_ENV}"
                sh "${env.VENV_ACTIVATE} && pip install -r requirements.txt"
                // Установка зависимостей для тестов
                sh "${env.VENV_ACTIVATE} && pip install -r tests/requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                // Запуск тестов с использованием pytest
                sh "${env.VENV_ACTIVATE} && pytest --pyargs tests"
            }
        }
    }

    post {
        success {
            echo 'Build and tests succeeded!'
        }
        failure {
            echo 'Build or tests failed!'
        }
        always {
            // Очистка рабочей области после выполнения
            cleanWs()
        }
    }
}
