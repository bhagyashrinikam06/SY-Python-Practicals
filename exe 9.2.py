grades = [75, 82, 68, 90, 55]

old = int(input("Enter grade to change: "))
new = int(input("Enter new grade: "))

if old in grades:
    grades[grades.index(old)] = new

print("Corrected grades:", grades)
