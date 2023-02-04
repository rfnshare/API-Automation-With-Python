import paramiko as paramiko
from pathlib import Path

from utilities.config import getConfig, uploadIntoAWS, getSSHConnection
# Setup AWS
# ec2-54-178-192-48.ap-northeast-1.compute.amazonaws.com [Host]
# ec2-user [user]
# sudo su - [go to root user]
# vi /etc/ssh/sshd_config []
# service sshd reload [to effect system]
# passwd ec2-user [setup password for ec2-user]


# Start Connection
ssh = getSSHConnection()

# Run Commands
stdin, stdout, stderr = ssh.exec_command("cat demoFile")
lines = stdout.readlines()
print(lines[1])

# Uploading Files
uploadIntoAWS('batchFiles/script.py', 'script.py')
uploadIntoAWS('batchFiles/loanasa.csv', 'loanasa.csv')

# Trigger The Batch
ssh.exec_command("python3 script.py")
ssh.close()
