from flask import Blueprint, request, session, jsonify

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username required"}), 400

    session["user"] = username

    return jsonify({"message": "Login successful", "user": username})

