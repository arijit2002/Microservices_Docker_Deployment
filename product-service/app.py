from flask import Flask, request, jsonify
import jwt
from functools import wraps

app = Flask(__name__)
SECRET_KEY = "mysecretkey"  # Must match Node.js secret

products = []
product_id_counter = 1

# JWT Middleware
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except Exception as e:
            return jsonify({"message": "Token is invalid!", "error": str(e)}), 401
        return f(*args, **kwargs)
    return decorated

# CRUD APIs
@app.route("/products", methods=["POST"])
@token_required
def add_product():
    global product_id_counter
    data = request.json
    product = {"id": product_id_counter, "name": data["name"], "price": data["price"]}
    products.append(product)
    product_id_counter += 1
    return jsonify(product)

@app.route("/products", methods=["GET"])
@token_required
def get_products():
    return jsonify(products)

@app.route("/products/<int:id>", methods=["PUT"])
@token_required
def update_product(id):
    data = request.json
    for product in products:
        if product["id"] == id:
            product["name"] = data.get("name", product["name"])
            product["price"] = data.get("price", product["price"])
            return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

@app.route("/products/<int:id>", methods=["DELETE"])
@token_required
def delete_product(id):
    global products
    products = [p for p in products if p["id"] != id]
    return jsonify({"message": "Product deleted"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
