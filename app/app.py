import time
import requests

API_URL = os.environ.get("API_URL", "http://api:5000")

def get_api_data():
    for _ in range(10):
        try:
            r = requests.get(f"{API_URL}/data")
            return r.json()
        except requests.exceptions.RequestException:
            time.sleep(1)
    return {"error": "API not reachable"}

@app.route('/')
def index():
    return jsonify({"status": "success", "api_data": get_api_data()})
