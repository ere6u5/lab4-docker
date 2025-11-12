from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.environ.get("DB_PATH", "/data/db.sqlite")

@app.route('/data')
def data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mytable;")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
