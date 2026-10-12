balance = 0

def add_funds(amount):
    global balance
    balance += amount

def pay_bill(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Bill paid successfully")
    else:
        print("Insufficient balance")

while True:
    print("\n1. Add Funds\n2. Pay Bill\n3. View Balance\n4. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_funds(float(input("Enter amount: ")))
    elif ch == 2:
        pay_bill(float(input("Enter bill amount: ")))
    elif ch == 3:
        print("Balance:", balance)
    elif ch == 4:
        break
    else:
        print("Invalid choice")