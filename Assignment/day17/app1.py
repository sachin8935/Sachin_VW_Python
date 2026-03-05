from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        if name == "" or email == "" or password == "":
            message = "Fields should not be blank"

        elif "@" not in email:
            message = "Email must contain @"

        elif len(password) < 5 or len(password) > 8:
            message = "Password must be between 5 and 8 characters"

        else:
            message = "Form submitted successfully"

    return render_template("index1.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)

