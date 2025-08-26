from flask import Flask, jsonify, request
from controllers import UserController

user_controller = UserController()

app = Flask(__name__)

@app.route("/home/user/login", methods=["GET"])
def login():
    return user_controller.login_user()

@app.route("/home/user/<string:id_user>", methods=["GET"])
def select(id_user: str):
    return user_controller.select_user(id_user)

@app.route("/home/user/<string:id_user>", methods=["DELETE"])
def delete(id_user: str):
    return user_controller.delete_user(id_user)

@app.route("/home/user/register", methods=["POST"])
def register():
    return user_controller.add_user()

@app.route("/home/user/update/<string:id_user>", methods=["PUT"])
def update(id_user: str):
    return user_controller.update_user(id_user)

@app.route("/home", methods=["GET"])
def home():
    return jsonify({
        "version": "1.0.0",
        "name": "API - Render" 
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)