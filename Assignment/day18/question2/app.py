
from flask import Flask
from auth import auth
from products import products_bp

app = Flask(__name__)
app.secret_key = "secretkey"

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(products_bp)

if __name__ == "__main__":
    app.run(debug=True)

