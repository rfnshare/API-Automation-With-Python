import csv
from utilities.config import *

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

# Download Local Files to local systems
downloadFromAWS('loanasa.csv', 'batchFiles/output/loanasa.csv')
ssh.close()

with open(Path(__file__).parent.parent / 'batchFiles/output/loanasa.csv') as f:
    f = csv.reader(f, delimiter=',')
    names = []
    status = []
    for i in f:
        names.append(i[0])
        status.append(i[1])

dic = dict(zip(names, status))
# print(dic)
# print(status)
for x, y in dic.items():
    if x == '32321':
        assert y == 'rejected'
