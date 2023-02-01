import mysql.connector

# host, db, user, password
conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='p@ssw0rd')
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('SELECT * FROM CustomerInfo')
# row = cursor.fetchone()
# print(row[3])
row = cursor.fetchall()
print(len(row))
add = 0
for i in row:
    add += i[2]
print(add)
conn.close()
