import secrets

n = int(input("Enter number of dice: "))
rolls = [secrets.randbelow(6) + 1 for _ in range(n)]

print("Dice outcomes:", rolls)
print("Total score:", sum(rolls))