pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo $Hello'
      }
    }

    stage('Testing') {
      parallel {
        stage('Testing A') {
          steps {
            sh 'echo Testing A'
          }
        }

        stage('Testing B') {
          steps {
            sh 'echo Testing B'
          }
        }

      }
    }

  }
  environment {
    Hello = 'Welcome to Jenkins'
  }
}