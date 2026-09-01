transactions = [float(input(f"Transaction {i+1}: ")) for i in range(5)]

print("Largest:", max(transactions))
print("Average:", sum(transactions) / 5)
