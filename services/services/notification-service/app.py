from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "notification-service",
        "status": "running"
    })

@app.route("/notifications")
def notifications():
    return jsonify({
        "notifications": [
            {"id": 1, "message": "Order confirmed", "status": "sent"},
            {"id": 2, "message": "Payment completed", "status": "sent"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
