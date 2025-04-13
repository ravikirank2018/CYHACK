from flask import Flask, request, jsonify, render_template
import sqlite3
import openai
import numpy as np
from sklearn.ensemble import IsolationForest

app = Flask(__name__)
openai.api_key = "your_openai_api_key"

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reports', methods=['GET'])
def get_reports():
    conn = get_db_connection()
    transactions = conn.execute('SELECT * FROM transactions').fetchall()
    conn.close()
    return jsonify([dict(tx) for tx in transactions])

@app.route('/ai', methods=['POST'])
def ai_chat():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": data['message']}]
    )
    return jsonify({"reply": response["choices"][0]["message"]["content"]})

@app.route('/fraud-detection', methods=['GET'])
def detect_fraud():
    conn = get_db_connection()
    transactions = conn.execute('SELECT amount FROM transactions').fetchall()
    conn.close()
    amounts = np.array([tx['amount'] for tx in transactions]).reshape(-1, 1)
    model = IsolationForest(contamination=0.1)
    model.fit(amounts)
    anomalies = model.predict(amounts)
    fraud_transactions = [dict(tx) for idx, tx in enumerate(transactions) if anomalies[idx] == -1]
    return jsonify(fraud_transactions)

@app.route('/scan-qr', methods=['POST'])
def scan_qr():
    data = request.json
    qr_code_data = data.get("qr_code_data", "")
    return jsonify({"message": "QR Code Scanned Successfully", "data": qr_code_data})

if __name__ == '__main__':
    app.run(debug=True)
