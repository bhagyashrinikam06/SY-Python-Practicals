m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("\n--- Student Scorecard ---")
print("Total Marks:", total)
print("Average:", round(average, 2))