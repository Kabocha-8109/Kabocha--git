import sqlite3

conn = sqlite3.connect('DevOps.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM product_info')
records =  cursor.fetchall()
print (records)