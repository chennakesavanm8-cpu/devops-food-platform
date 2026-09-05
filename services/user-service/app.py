from flask import Flask, jsonify
import urllib.request
import json

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "user-service",
        "status": "running"
    })


@app.route("/users")
def users():
    return jsonify({
        "users": [
            {"id": 1, "name": "Kesavan"},
            {"id": 2, "name": "DevOps User"}
        ]
    })


@app.route("/user-orders")
def user_orders():
    response = urllib.request.urlopen(
        "http://order-service:5001/orders"
    )

    data = response.read().decode("utf-8")
    orders = json.loads(data)

    return jsonify({
        "users": [
            {"id": 1, "name": "Kesavan"},
            {"id": 2, "name": "DevOps User"}
        ],
        "orders": orders
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
