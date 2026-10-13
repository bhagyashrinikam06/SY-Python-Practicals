def lookup_item(data):
    key = input("Enter item name: ")

    try:
        print("Value:", data[key])

    except KeyError:
        print("Item Not Found")

data = {
    "apple": 50,
    "banana": 30,
    "mango": 60
}

lookup_item(data)