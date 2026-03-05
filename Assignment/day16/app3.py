from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    students = [
        {"name": "John", "marks": 80},
        {"name": "Amit", "marks": 40}
    ]
    return render_template("index3.html", students=students)

app.run(debug=True)