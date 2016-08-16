node 
  {
  stage 'Checkout'
    git url: 'https://github.com/fm75/performance/'
    
  stage 'Environment'
    sh 'env'

  stage 'CPU Test'
    sh '/var/lib/jenkins/jobs/SpeedPipe/workspace/cpu.py'
   
  stage 'I/O Test'
    sh '/var/lib/jenkins/jobs/SpeedPipe/workspace/io.py'
  }
