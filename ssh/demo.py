import paramiko as paramiko

from utilities.config import getConfig

# ec2-54-178-192-48.ap-northeast-1.compute.amazonaws.com [Host]
# ec2-user [user]
# sudo su - [go to root user]
# vi /etc/ssh/sshd_config []
# service sshd reload [to effect system]
# passwd ec2-user [setup password for ec2-user]

username = getConfig()['SSH']['username']
password = getConfig()['SSH']['password']
host = getConfig()['SSH']['host']
port = getConfig()['SSH']['port']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
