inventory = {}

def add_stock():
    item = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    inventory[item] = inventory.get(item, 0) + qty
    print("Stock added")

def register_sale():
    item = input("Enter item name: ")
    qty = int(input("Enter quantity sold: "))
    if inventory.get(item, 0) >= qty:
        inventory[item] -= qty
        print("Sale registered")
    else:
        print("Insufficient stock")

def show_inventory():
    print("Current Inventory:", inventory)

while True:
    print("\n1. Add Stock\n2. Register Sale\n3. View Inventory\n4. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_stock()
    elif ch == 2:
        register_sale()
    elif ch == 3:
        show_inventory()
    elif ch == 4:
        break
    else:
        print("Invalid choice")