from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/home", methods=["GET"])
def home():
    return jsonify({
        "version": "1.0.0",
        "name": "API - Render" 
    }), 200

@app.route("/home/login", methods=["GET"])
def login():
    return jsonify(
        request.args
    ), 200

@app.route("/home/cadaster", methods=["POST"])
def cadaster():
    return jsonify(
        request.json
    ), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)