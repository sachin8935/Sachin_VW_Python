from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":
        name = request.form["name"]

        visit = request.cookies.get(name)

        if visit:
            visit = int(visit) + 1
        else:
            visit = 1

        response = make_response(render_template("index2.html", name=name, visit=visit))
        response.set_cookie(name, str(visit))

        return response

    return render_template("index2.html")


if __name__ == "__main__":
    app.run(debug=True)


