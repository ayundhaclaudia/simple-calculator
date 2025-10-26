pipeline {
  agent any
  environment {
    IMAGE_NAME = 'yourusername/simple-calculator'
    REGISTRY = 'https://index.docker.io/v1/'
    REGISTRY_CREDENTIALS = 'dockerhub-credentials'
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build') {
      steps {
        sh 'echo "Mulai build kalkulator sederhana"'
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
          docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
        }
      }
    }
    stage('Push Docker Image') {
      steps {
        script {
          docker.withRegistry(REGISTRY, REGISTRY_CREDENTIALS) {
            def tag = "${IMAGE_NAME}:${env.BUILD_NUMBER}"
            docker.image(tag).push()
            docker.image(tag).push('latest')
          }
        }
      }
    }
  }
  post {
    always { echo 'Selesai build kalkulator sederhana' }
  }
}
