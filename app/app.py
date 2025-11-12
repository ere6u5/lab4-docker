from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

API_URL = os.environ.get("API_URL", "http://api:5000")

@app.route('/')
def index():
    try:
        r = requests.get(f"{API_URL}/data")
        return jsonify({"status": "success", "api_data": r.json()})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8181)
