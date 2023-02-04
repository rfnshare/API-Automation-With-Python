import configparser

import paramiko
from mysql.connector import Error
from pathlib import Path
import mysql.connector


def getConfig():
    config = configparser.ConfigParser()
    config.read(Path(__file__).parent.parent / 'utilities/properties.ini')
    return config


# host, db, user, password
connect_config = {
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database']
}


# ssh_connect_config = {
#     'host': getConfig()['SSH']['host'],
#     'port': getConfig()['SSH']['port'],
#     'username': getConfig()['SSH']['username'],
#     'password': getConfig()['SSH']['password']
# }

def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connected")
            return conn
    except Error as e:
        print("Error->", e)


username = getConfig()['SSH']['username']
password = getConfig()['SSH']['password']
host = getConfig()['SSH']['host']
port = getConfig()['SSH']['port']


def getSSHConnection():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    return ssh


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row


def uploadIntoAWS(src, dest):
    ssh = getSSHConnection()
    sftp = ssh.open_sftp()
    des_path = dest
    src_path = (Path(__file__).parent.parent / src)
    sftp.put(src_path, des_path)
