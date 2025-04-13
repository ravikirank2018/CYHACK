import mysql.connector
import json

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='2004',
    database='cyber_incidents_db'
)

cursor = conn.cursor()


with open('incidents.json') as f:
    data = json.load(f)


for incident in data:
    title = incident.get('title')
    date = incident.get('date')
    details = incident.get('details')

    
    sql = "INSERT INTO incidents (title, date, details) VALUES (%s, %s, %s)"
    cursor.execute(sql, (title, date, details))

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully into MySQL database!")
