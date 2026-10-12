def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

while True:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", celsius_to_fahrenheit(c))
    elif ch == 2:
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", fahrenheit_to_celsius(f))
    elif ch == 3:
        break
    else:
        print("Invalid choice")