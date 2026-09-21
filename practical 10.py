products = {
    101: ["Laptop", 55000],
    102: ["Mobile", 25000],
    103: ["Keyboard", 1200],
    104: ["Mouse", 800],
    105: ["Headphones", 2000]
}


while True:

    print("\n========== INVENTORY SYSTEM ==========")
    print("1. Display Products")
    print("2. Search Product")
    print("3. Sort Products by Price")
    print("4. Add Product")
    print("5. Update Product Price")
    print("6. Delete Product")
    print("7. Exit")

    choice = int(input("\nEnter your choice: "))

    # 1. Display
    if choice == 1:

        print("\n----- Product List -----")

        for pid, details in products.items():
            print(
                "ID:", pid,
                "| Product:", details[0],
                "| Price: ₹", details[1]
            )

    # 2. Search
    elif choice == 2:

        search = input("Enter product name: ").lower()

        found = False

        for pid, details in products.items():

            if search in details[0].lower():

                print("\nProduct Found")
                print("ID:", pid)
                print("Product:", details[0])
                print("Price: ₹", details[1])

                found = True

        if not found:
            print("Product not found.")

    # 3. Sort
    elif choice == 3:

        print("\n1. Low to High")
        print("2. High to Low")

        sort_choice = int(input("Enter choice: "))

        if sort_choice == 1:

            sorted_products = sorted(
                products.items(),
                key=lambda x: x[1][1]
            )

        elif sort_choice == 2:

            sorted_products = sorted(
                products.items(),
                key=lambda x: x[1][1],
                reverse=True
            )

        else:
            print("Invalid choice.")
            continue

        print("\n----- Sorted Products -----")

        for pid, details in sorted_products:
            print(
                "ID:", pid,
                "| Product:", details[0],
                "| Price: ₹", details[1]
            )

    # 4. Add
    elif choice == 4:

        pid = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))

        products[pid] = [name, price]

        print("Product added successfully!")

    # 5. Update Price
    elif choice == 5:

        pid = int(input("Enter Product ID: "))

        if pid in products:

            new_price = float(input("Enter new price: "))

            products[pid][1] = new_price

            print("Price updated successfully!")

        else:
            print("Product not found.")

    # 6. Delete
    elif choice == 6

        pid = int(input("Enter Product ID: "))

        if pid in products:

            del products[pid]

            print("Product deleted successfully!")

        else:
            print("Product not found.")

    # 7. Exit
    elif choice == 7:

        print("Thank you for using Inventory System!")
        break

    else:

        print("Invalid choice. Please enter 1 to 7.")
