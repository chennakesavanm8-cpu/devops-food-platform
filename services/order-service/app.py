from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "order-service",
        "status": "running"
    })

@app.route("/orders")
def orders():
    return jsonify({
        "orders": [
            {"id": 1, "item": "Pizza"},
            {"id": 2, "item": "Burger"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
