from flask import Flask, render_template, request

app = Flask(__name__)

employees = [
    {"name": "Amit", "department": "IT", "salary": 50000},
    {"name": "Neha", "department": "HR", "salary": 45000},
    {"name": "Raj", "department": "Finance", "salary": 55000},
]

@app.route("/dashboard")
def dashboard():
    role = request.args.get("role", "employee").lower()

    return render_template(
        "index5.html",
        role=role,
        employees=employees
    )

if __name__ == "__main__":
    app.run(debug=True)
