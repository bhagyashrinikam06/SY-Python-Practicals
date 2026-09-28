# 3x3 seating grid
seats = [["o" for _ in range(3)] for _ in range(3)]

while True:
    print("\nSeating Layout:")
    for row in seats:
        print(" ".join(row))

    r = int(input("Enter row (0-2): "))
    c = int(input("Enter column (0-2): "))

    if 0 <= r < 3 and 0 <= c < 3:
        if seats[r][c] == "o":
            seats[r][c] = "x"
            print("Seat reserved!")
        else:
            print("Seat already reserved.")
    else:
        print("Invalid seat.")

    if input("Book another seat? (y/n): ").lower() != "y":
        break
