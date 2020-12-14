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

    stage('Waiting for approval') {
      steps {
        input(message: 'Please approve', ok: 'Lets do it!')
      }
    }

  }
  environment {
    Hello = 'Welcome to Jenkins'
  }
}