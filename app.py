from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


products = [
    {
        "id": 1,
        "name": "Canvas Tote Bag",
        "price": 399,
        "quantity": 18,
        "category": "Accessories",
        "description": "Durable everyday tote made with recycled canvas.",
    },
    {
        "id": 2,
        "name": "Desk Lamp",
        "price": 1299,
        "quantity": 9,
        "category": "Home",
        "description": "Adjustable LED lamp with three brightness modes.",
    },
    {
        "id": 3,
        "name": "Wireless Mouse",
        "price": 699,
        "quantity": 24,
        "category": "Electronics",
        "description": "Compact mouse with silent clicks and USB receiver.",
    },
]


next_product_id = 4


def find_product(product_id):
    return next((product for product in products if product["id"] == product_id), None)


def validate_product_payload(data, is_update=False):
    errors = {}
    required_fields = ["name", "price", "quantity", "category", "description"]

    if not isinstance(data, dict):
        return {"body": "Request body must be a JSON object."}

    if not is_update:
        for field in required_fields:
            if field not in data:
                errors[field] = f"{field.title()} is required."

    if "name" in data and not str(data["name"]).strip():
        errors["name"] = "Name cannot be empty."

    if "category" in data and not str(data["category"]).strip():
        errors["category"] = "Category cannot be empty."

    if "description" in data and not str(data["description"]).strip():
        errors["description"] = "Description cannot be empty."

    if "price" in data:
        try:
            price = float(data["price"])
            if price <= 0:
                errors["price"] = "Price must be greater than zero."
        except (TypeError, ValueError):
            errors["price"] = "Price must be a valid number."

    if "quantity" in data:
        try:
            quantity = int(data["quantity"])
            if quantity < 0:
                errors["quantity"] = "Quantity cannot be negative."
        except (TypeError, ValueError):
            errors["quantity"] = "Quantity must be a valid whole number."

    return errors


def build_product(data, product_id):
    return {
        "id": product_id,
        "name": str(data["name"]).strip(),
        "price": float(data["price"]),
        "quantity": int(data["quantity"]),
        "category": str(data["category"]).strip(),
        "description": str(data["description"]).strip(),
    }


@app.get("/")
def health_check():
    return jsonify({"message": "Shopy backend is running."})


@app.get("/api/products")
def get_products():
    search = request.args.get("search", "").strip().lower()
    category = request.args.get("category", "").strip().lower()

    filtered_products = products
    if search:
        filtered_products = [
            product
            for product in filtered_products
            if search in product["name"].lower()
            or search in product["description"].lower()
            or search in product["category"].lower()
        ]

    if category:
        filtered_products = [
            product
            for product in filtered_products
            if product["category"].lower() == category
        ]

    return jsonify({"products": filtered_products, "count": len(filtered_products)})


@app.get("/api/products/<int:product_id>")
def get_product(product_id):
    product = find_product(product_id)
    if product is None:
        return jsonify({"message": "Product not found."}), 404

    return jsonify({"product": product})


@app.post("/api/products")
def create_product():
    global next_product_id

    data = request.get_json(silent=True)
    errors = validate_product_payload(data)
    if errors:
        return jsonify({"message": "Invalid product data.", "errors": errors}), 400

    product = build_product(data, next_product_id)
    products.append(product)
    next_product_id += 1

    return jsonify({"message": "Product created successfully.", "product": product}), 201


@app.put("/api/products/<int:product_id>")
def update_product(product_id):
    product = find_product(product_id)
    if product is None:
        return jsonify({"message": "Product not found."}), 404

    data = request.get_json(silent=True)
    errors = validate_product_payload(data, is_update=True)
    if errors:
        return jsonify({"message": "Invalid product data.", "errors": errors}), 400

    updated_data = {**product, **data}
    product.update(build_product(updated_data, product_id))

    return jsonify({"message": "Product updated successfully.", "product": product})


@app.delete("/api/products/<int:product_id>")
def delete_product(product_id):
    product = find_product(product_id)
    if product is None:
        return jsonify({"message": "Product not found."}), 404

    products.remove(product)
    return jsonify({"message": "Product deleted successfully.", "product": product})


if __name__ == "__main__":
    app.run(debug=True, port=5050)
