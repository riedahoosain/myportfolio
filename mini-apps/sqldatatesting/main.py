import sqlite3

# Establish a connection
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Query Data
cursor.execute("SELECT * FROM events WHERE date='2088.10.14'")
rows = cursor.fetchall()
print(rows)

# Query Certain columns
cursor.execute("SELECT date,band FROM events WHERE date='2088.10.14'")
rows = cursor.fetchall()
print(rows)

# Query Data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)

# Insert data
new_rows = [('Rabbit', 'Rabbit City', '2088.10.16'),
            ('Bears', 'Bear City', '2088.10.16'),
            ('Bulls', 'Bulls City', '2088.10.17')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()
