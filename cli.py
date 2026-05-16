import requests

BASE_URL = "http://127.0.0.1:5000"

def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    print(response.json())

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    stock = int(input("Enter stock amount: "))

    new_item = {
        "name": name,
        "price": price,
        "stock": stock
    }

    response = requests.post(f"{BASE_URL}/inventory", json=new_item)
    print(response.json())

def delete_item():
    item_id = input("Enter item ID to delete: ")

    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")
    print(response.json())

def search_food():
    barcode = input("Enter barcode: ")

    response = requests.get(f"{BASE_URL}/food/{barcode}")
    print(response.json())

while True:
    print("\nInventory Management System")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Delete Item")
    print("4. Search Food by Barcode")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_inventory()
    elif choice == "2":
        add_item()

    elif choice == "3":
        delete_item()

    elif choice == "4":
        search_food()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
