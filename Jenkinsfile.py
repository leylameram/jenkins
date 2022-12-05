from cProfile import label

import agent
from pipeline.pipeline import pipeline
from stages import stages

pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                echo "Hello World!"
            }
        }
    }
}