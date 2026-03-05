

from flask import Blueprint, jsonify, request, session, make_response
import json

products = [
    {"id":1,"name":"Laptop","price":70000},
    {"id":2,"name":"Mouse","price":500},
    {"id":3,"name":"Keyboard","price":1200}
]

products_bp = Blueprint("products", __name__)

# API 2: Get all products
@products_bp.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


# API 3: View product
@products_bp.route("/products/<int:product_id>", methods=["GET"])
def view_product(product_id):

    if "user" not in session:
        return jsonify({"error":"Login required"}),401

    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error":"Product not found"}),404

    recent = request.cookies.get("recent_products")

    if recent:
        recent = json.loads(recent)
    else:
        recent = []

    if product_id in recent:
        recent.remove(product_id)

    recent.append(product_id)

    if len(recent) > 5:
        recent.pop(0)

    response = make_response(jsonify(product))
    response.set_cookie("recent_products", json.dumps(recent))

    return response


# API 4: Get recently viewed products
@products_bp.route("/recent-products", methods=["GET"])
def recent_products():

    recent = request.cookies.get("recent_products")

    if not recent:
        return jsonify([])

    recent = json.loads(recent)

    result = [p for p in products if p["id"] in recent]

    return jsonify(result)


