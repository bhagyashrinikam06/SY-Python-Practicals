inventory = {
    "Pen": 10,
    "Book": 5,
    "Pencil": 3
}
item = input("Enter item sold: ")
quantity = int(input("Enter quantity sold: "))
if item in inventory:
    inventory[item] -= quantity
    if inventory[item] == 0:
        print("Warning: Stock is zero!")
    elif inventory[item] < 0:
        print("Not enough stock!")
        inventory[item] += quantity
    else:
        print("Remaining stock:", inventory[item])
else:
    print("Item not found.")
print("Inventory:", inventory)