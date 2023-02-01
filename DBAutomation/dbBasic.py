import mysql.connector

# host, db, user, password
conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='p@ssw0rd')
print(conn.is_connected())
cursor = conn.cursor()

# Read
cursor.execute('SELECT * FROM CustomerInfo')
# row = cursor.fetchone()
# print(row[3])
row = cursor.fetchall()
print(len(row))
add = 0
for i in row:
    add += i[2]
print(add)

# Update
query = "UPDATE CustomerInfo SET Location = %s WHERE CourseName = %s"
data = ("BD", "Jmeter")
cursor.execute(query, data)
conn.commit()

# Delete
query2 = "DELETE FROM CustomerInfo WHERE CourseName = %s"
data = ["Appium"]
cursor.execute(query2, data)
conn.commit()
conn.close()
