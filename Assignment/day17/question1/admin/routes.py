
from flask import Blueprint, request, redirect

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/dashboard")
def dashboard():

    role = request.cookies.get("user_role")

    if role != "admin":
        return redirect("/")

    username = request.cookies.get("username")

    return f"""
    <h2>Welcome Admin {username}</h2>
    <a href="/logout"><button>Logout</button></a>
    """
