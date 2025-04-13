from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

alerts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    alerts.append(data)
    return jsonify({'status': 'success'}), 200

@app.route('/alerts')
def get_alerts():
    return jsonify(alerts), 200

if __name__ == '__main__':
    app.run(debug=True)
