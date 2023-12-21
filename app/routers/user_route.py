# app/routers/user_route.py
from flask import Blueprint, request, jsonify

# Create a Blueprint instance
bp = Blueprint("user", __name__)

# Example data structure to store user information (in-memory)
users = []


@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    new_user = {"username": username, "password": password}
    users.append(new_user)

    return jsonify({"message": "User registered successfully"}), 201


@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = next((user for user in users if user["username"] == username), None)

    if user and user["password"] == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401


@bp.route("/profile/<username>", methods=["GET"])
def get_profile(username):
    user = next((user for user in users if user["username"] == username), None)

    if user:
        return jsonify({"username": user["username"]})
    else:
        return jsonify({"error": "User not found"}), 404
