from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

inventory = [
{
"id": 1,
"name": "Organic Almond Milk",
"brand": "Silk",
"price": 4.99,
"stock": 10
},
{
"id": 2,
"name": "Peanut Butter",
"brand": "Jif",
"price": 3.49,
"stock": 15
}
]

# GET all inventory
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)

# GET single item
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404

# POST new item
@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    new_item = {
        "id": len(inventory) + 1,
        "name": data["name"],
        "brand": data["brand"],
        "price": data["price"],
        "stock": data["stock"]
}

    inventory.append(new_item)

    return jsonify(new_item), 201

# PATCH item
@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    data = request.get_json()

    for item in inventory:
        if item["id"] == item_id:

            item["name"] = data.get("name", item["name"])
            item["brand"] = data.get("brand", item["brand"])
            item["price"] = data.get("price", item["price"])
            item["stock"] = data.get("stock", item["stock"])

            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404

# DELETE item
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Item deleted"})

    return jsonify({"error": "Item not found"}), 404

# External API route
@app.route("/food/<barcode>", methods=["GET"])
def get_food(barcode):

    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data.get("status") == 1:

            product = data["product"]

            return jsonify({
                "product_name": product.get("product_name"),
                "brands": product.get("brands"),
                "ingredients": product.get("ingredients_text")
            })

    return jsonify({"error": "Food not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
