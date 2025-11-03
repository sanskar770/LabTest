from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Serve a simple webpage directly from Flask
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Real-Time Health Monitoring</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background: linear-gradient(135deg, #1f1c2c, #928dab);
                color: #fff;
                padding: 50px;
            }
            h1 { font-size: 2em; }
            .data-box {
                background: rgba(255,255,255,0.1);
                padding: 20px;
                margin: 10px auto;
                width: 250px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(255,255,255,0.3);
            }
            span { font-weight: bold; font-size: 1.4em; }
        </style>
        <script>
            async function fetchData() {
                const response = await fetch('/get_data');
                const data = await response.json();
                document.getElementById('heart_rate').innerText = data.heart_rate + " bpm";
                document.getElementById('spo2').innerText = data.spo2 + " %";
                document.getElementById('temperature').innerText = data.temperature + " °C";
            }
            setInterval(fetchData, 2000); // Fetch every 2 seconds
            window.onload = fetchData;
        </script>
    </head>
    <body>
        <h1>🩺 Real-Time Health Monitoring</h1>
        <div class="data-box">
            <h2>Heart Rate: <span id="heart_rate">--</span></h2>
        </div>
        <div class="data-box">
            <h2>SpO₂: <span id="spo2">--</span></h2>
        </div>
        <div class="data-box">
            <h2>Temperature: <span id="temperature">--</span></h2>
        </div>
    </body>
    </html>
    """

# Simulate live data API endpoint
@app.route('/get_data')
def get_data():
    data = {
        'heart_rate': random.randint(60, 120),
        'spo2': random.randint(90, 100),
        'temperature': round(random.uniform(36.0, 38.0), 1)
    }
    return jsonify(data)

# Optional: receive POST requests (e.g., from sensors)
@app.route('/submit', methods=['POST'])
def submit():
    content = request.get_json()
    print("Received Data:", content)
    return jsonify({'status': 'success', 'message': 'Data received successfully!'})

if __name__ == '__main__':
    app.run(debug=True)

        



        
