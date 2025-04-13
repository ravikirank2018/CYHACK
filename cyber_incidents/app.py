from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch incidents data from the database
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2004',
            database='cyber_incidents_db'
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM incidents")  # Fetch incidents from the database
        incidents = cursor.fetchall()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        incidents = []  # Set to empty list if there's an error fetching data

    return render_template('index.html', incidents=incidents)  # Pass incidents to the template

if __name__ == "__main__":
    app.run(debug=True)
