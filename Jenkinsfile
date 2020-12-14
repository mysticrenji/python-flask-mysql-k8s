pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo $Hello'
      }
    }

  }
  environment {
    Hello = 'Welcome to Jenkins'
  }
}