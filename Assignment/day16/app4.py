from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory product data
products = [
    {"name": "Laptop", "category": "Electronics", "price": 60000, "available": True},
    {"name": "Phone", "category": "Electronics", "price": 25000, "available": True},
    {"name": "Shoes", "category": "Fashion", "price": 3000, "available": False},
    {"name": "T-Shirt", "category": "Fashion", "price": 800, "available": True},
    {"name": "Watch", "category": "Accessories", "price": 2000, "available": True},
    {"name": "Bag", "category": "Accessories", "price": 1500, "available": False},
]

@app.route("/products")
def product_list():

    filtered_products = products.copy()

    # ✅ 1️⃣ Filter by category
    category = request.args.get("category")
    if category:
        filtered_products = [
            p for p in filtered_products if p["category"].lower() == category.lower()
        ]

    # ✅ 2️⃣ Filter by availability
    availability = request.args.get("available")
    if availability:
        is_available = availability.lower() == "true"
        filtered_products = [
            p for p in filtered_products if p["available"] == is_available
        ]

    # ✅ 3️⃣ Sort by price
    sort_order = request.args.get("sort")

    if sort_order == "low":
        filtered_products.sort(key=lambda x: x["price"])

    elif sort_order == "high":
        filtered_products.sort(key=lambda x: x["price"], reverse=True)

    # ✅ 4️⃣ Count results
    total = len(filtered_products)

    return render_template(
        "index4.html",
        products=filtered_products,
        total=total
    )

if __name__ == "__main__":
    app.run(debug=True)