node 
  {
  stage 'Checkout'
    git url: 'https://github.com/fm75/performance/'
    
  stage 'Unit Tests'
    sh 'env'

  stage 'Build'
    sh 'env'

  stage 'Package'
    sh 'env'

  stage 'Deploy'
    sh 'env'

  stage 'Halt Service'
    sh 'env'

  stage 'Start Service'
    sh 'env'

  stage 'Integration Testing'
    sh 'env'

  stage 'CPU Performance Test'
    sh './cpu.py'
   
  stage 'I/O Performance Test'
    sh './io.py'
    
  stage 'Commit to Master Branch'
    timeout(time:5, unit:'DAYS') {
    input message:'Approve deployment?', submitter: 'fred'
    }

  stage 'Checkout'
    //git url: 'https://github.com/fm75/performance/'
    sh 'env'
    
  stage 'Unit Tests'
    sh 'env'

  stage 'Build'
    sh 'env'

  stage 'Package'
    sh 'env'

  stage 'Deploy'
    sh 'env'

  stage 'Halt Service'
    sh 'env'

  stage 'Start Service'
    sh 'env'

  stage 'Integration Testing'
    sh 'env'

  stage 'CPU Performance Test'
    sh './cpu.py'
   
  stage 'I/O Performance Test'
    sh './io.py'
    
  stage 'Production Orchestration'
    sh 'env'

  }
