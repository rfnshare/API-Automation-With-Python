import mysql.connector

# host, db, user, password
conn = mysql.connector.connect(host='localhost', database='PythonAutomation', user='root', password='p@ssw0rd')
print(conn.is_connected())
