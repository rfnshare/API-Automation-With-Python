import configparser
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


def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connected")
            return conn
    except Error as e:
        print("Error->", e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
