

from flask import Blueprint, render_template, request, redirect, make_response
import json

products_bp = Blueprint("products", __name__)

products_list = {
    "laptop": 80000,
    "mouse": 500,
    "keyboard": 1500,
    "monitor": 12000,
    "headphones": 2000
}

@products_bp.route("/")
def show_products():
    return render_template("products.html", products=products_list)


@products_bp.route("/add/<product>")
def add_to_cart(product):

    cart_cookie = request.cookies.get("cart")

    if cart_cookie:
        cart = json.loads(cart_cookie)
    else:
        cart = {}

    cart[product] = cart.get(product, 0) + 1

    response = make_response(redirect("/cart"))
    response.set_cookie("cart", json.dumps(cart))

    return response