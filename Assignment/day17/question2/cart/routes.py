from flask import Blueprint, request, render_template, make_response, redirect
import json

cart_bp = Blueprint("cart", __name__)

prices = {
    "laptop": 80000,
    "mouse": 500,
    "keyboard": 1500,
    "monitor": 12000,
    "headphones": 2000
}

@cart_bp.route("/")
def view_cart():

    cart_cookie = request.cookies.get("cart")

    if not cart_cookie:
        return "Cart is empty"

    cart = json.loads(cart_cookie)

    items = []
    total = 0

    for product, qty in cart.items():
        price = prices[product]
        total += price * qty
        items.append((product, qty, price))

    return render_template("cart.html", items=items, total=total)


@cart_bp.route("/increase/<product>")
def increase(product):

    cart = json.loads(request.cookies.get("cart"))
    cart[product] += 1

    response = make_response(redirect("/cart"))
    response.set_cookie("cart", json.dumps(cart))

    return response


@cart_bp.route("/decrease/<product>")
def decrease(product):

    cart = json.loads(request.cookies.get("cart"))

    if cart[product] > 1:
        cart[product] -= 1
    else:
        del cart[product]

    response = make_response(redirect("/cart"))
    response.set_cookie("cart", json.dumps(cart))

    return response


@cart_bp.route("/clear")
def clear_cart():

    response = make_response(redirect("/cart"))
    response.delete_cookie("cart")

    return response




