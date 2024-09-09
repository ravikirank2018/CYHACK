import mysql.connector
import json

# Load data from JSON file
with open('incidents.json') as f:
    data = json.load(f)

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',  # Replace with your MySQL username
    password='2004',  # Replace with your MySQL password
    database='cyber_incidents_db'
)

cursor = conn.cursor()

# SQL Insert statement
insert_query = """
INSERT INTO incidents (title, date, details)
VALUES (%s, %s, %s)
"""

# Insert each incident into the table
for incident in data:
    cursor.execute(insert_query, (incident['title'], incident['date'], incident['details']))

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Data inserted successfully.")
