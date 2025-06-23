from flask import Flask, render_template, jsonify, request
import json, os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/api/trades")
def get_trades():
    path = "live_trades.json"
    if os.path.exists(path):
        with open(path) as f:
            return jsonify(json.load(f))
    return jsonify([])

@app.route("/api/pnl")
def get_pnl():
    path = "pnl_summary.json"
    if os.path.exists(path):
        with open(path) as f:
            return jsonify(json.load(f))
    return jsonify({"total": 0})

@app.route("/api/stop", methods=["POST"])
def stop_bot():
    with open("stop_bot.flag", "w") as f:
        f.write("stop")
    return jsonify({"status": "stopped"})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
