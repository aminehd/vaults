"""
Mock server for Travel Optimization practice.

Endpoints:
  GET  /places?name=<str>         → { "place_id": "pid_<name>" }
  GET  /routes?from=<id>&to=<id>  → { "duration_minutes": <int> }

Run with:
  python mock_api_server.py
"""

from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# Deterministic fake driving times based on place id pair
def fake_duration(from_id, to_id):
    key = "".join(sorted([from_id, to_id]))
    h = int(hashlib.md5(key.encode()).hexdigest(), 16)
    return 10 + (h % 120)  # 10–129 minutes

@app.route("/places")
def get_place_id():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "missing name"}), 400
    return jsonify({"place_id": f"pid_{name.lower().replace(' ', '_')}"})

@app.route("/routes")
def get_route():
    from_id = request.args.get("from")
    to_id   = request.args.get("to")
    if not from_id or not to_id:
        return jsonify({"error": "missing from/to"}), 400
    if from_id == to_id:
        return jsonify({"duration_minutes": 0})
    return jsonify({"duration_minutes": fake_duration(from_id, to_id)})

if __name__ == "__main__":
    app.run(port=5001, debug=False)
