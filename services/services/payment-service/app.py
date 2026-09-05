from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "payment-service",
        "status": "running"
    })

@app.route("/payments")
def payments():
    return jsonify({
        "payments": [
            {"id": 1, "order_id": 1, "amount": 250, "status": "completed"},
            {"id": 2, "order_id": 2, "amount": 180, "status": "completed"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
