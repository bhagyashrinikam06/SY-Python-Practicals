# Active Inventory Catalogue Manager

def search_inventory(products, item_name):
    # Search for the item
    for index, product in enumerate(products):
        if product.lower() == item_name.lower():
            print(f"\nItem '{item_name}' is present in the inventory.")
            print(f"Index location: {index}")
            return

    # Item not found
    print(f"\nItem '{item_name}' was not found in the inventory.")


# Product catalogue
products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Printer",
    "Headphones"
]

# Display catalogue
print("Inventory Catalogue:")
for index, product in enumerate(products):
    print(f"{index}: {product}")

# Get item from user
item_name = input("\nEnter the item name to search: ")

# Search the inventory
search_inventory(products, item_name)
