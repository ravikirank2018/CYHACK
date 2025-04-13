from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='2004',  
        database='cyber_incidents_db'
    )

@app.route('/incidents', methods=['GET'])
def get_incidents():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM incidents ORDER BY date DESC')
    incidents = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(incidents)

if __name__ == '__main__':
    app.run(debug=True)
