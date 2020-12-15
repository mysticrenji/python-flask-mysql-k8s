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
            sh 'echo Testing A >> text.txt'
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
      parallel {
        stage('Waiting for approval') {
          steps {
            input(message: 'Please approve', ok: 'Lets do it!')
          }
        }

        stage('Archive') {
          steps {
            archiveArtifacts(fingerprint: true, artifacts: '**/*.txt', onlyIfSuccessful: true)
          }
        }

      }
    }

  }
  environment {
    Hello = 'Welcome to Jenkins'
  }
}