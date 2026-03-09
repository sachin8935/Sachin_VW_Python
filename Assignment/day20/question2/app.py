from flask import Flask
from models import db, Order

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/order_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Order": Order}

with app.app_context():
    db.create_all()