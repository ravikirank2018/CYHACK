import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='2004',
    database='cyber_incidents_db'
)

# Fetch data from MySQL
query = "SELECT * FROM incidents"
df = pd.read_sql(query, conn)


def categorize_sector(details):
    if 'healthcare' in details.lower():
        return 'Healthcare'
    elif 'financial' in details.lower():
        return 'Financial'
    elif 'tech' in details.lower() or 'software' in details.lower():
        return 'Technology'
    elif 'retail' in details.lower():
        return 'Retail'
    else:
        return 'Other'


df['sector'] = df['details'].apply(categorize_sector)


sector_counts = df['sector'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(sector_counts.index, sector_counts.values)
plt.xlabel('Sector')
plt.ylabel('Number of Incidents')
plt.title('Cyber Incidents by Sector')
plt.show()


conn.close()
