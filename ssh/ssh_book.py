from utilities.config import *

# Start Connection
ssh = getSSHConnection()

# Uploading Files
uploadIntoAWS('Web_Scrapping/book_details.py', 'book_details.py')

# Trigger The Batch
transport = ssh.get_transport()
channel = transport.open_session()
channel.exec_command('python3 book_details.py')
channel.recv_exit_status()
#
# status = channel.recv_exit_status()
# print("Script Stat:", status)

# Download Local Files to local systems
downloadFromAWS('output.csv', 'batchFiles/output/output_ssh.csv')
ssh.close()
