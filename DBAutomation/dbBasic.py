from utilities.config import getConnection

# Create a connection
conn = getConnection()
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
    print(i)
# assert add == 121
print("Total Amount", add)

# Update
# query = "UPDATE CustomerInfo SET Amount = %s WHERE CourseName = %s"
# data = (99, "Appium")
# cursor.execute(query, data)
# conn.commit()

# Delete
# query2 = "DELETE FROM CustomerInfo WHERE CourseName = %s"
# data = ["Appium"]
# cursor.execute(query2, data)
# conn.commit()
# conn.close()

# Create
# query3 = "INSERT INTO CustomerInfo values(%s,CURRENT_DATE(),21,%s)"
# data = ("Appium", "Germany")
# cursor.execute(query3, data)
# conn.commit()
# conn.close()
