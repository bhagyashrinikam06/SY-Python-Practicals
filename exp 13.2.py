students = {
    101: "student1@gmail.com",
    102: "student2@gmail.com",
    103: "student3@gmail.com"
}
roll = int(input("Enter roll number: "))
if roll in students:
    print("Email:", students[roll])
else:
   print("Student not found.")
