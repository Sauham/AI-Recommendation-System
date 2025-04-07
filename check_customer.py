import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM customers WHERE CustomerID = 1000")
result = cursor.fetchone()

if result:
    print("Customer Found:", result)
else:
    print("Customer not found")

conn.close()
