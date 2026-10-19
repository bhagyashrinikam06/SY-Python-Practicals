f = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

f.write("Name: " + name + "\n")
f.write("Roll Number: " + roll + "\n")
f.write("Marks: " + marks + "\n")

f.close()

print("\nStudent Record Saved Successfully!")

f = open("student.txt", "r")

print("\nStudent Details:")
print(f.read())

f.close()