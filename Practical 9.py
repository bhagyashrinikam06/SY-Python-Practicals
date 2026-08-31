marks = []

while True:
    print("\n===== STUDENT MARKS MANAGEMENT SYSTEM =====")
    print("1. Insert Marks")
    print("2. Display Marks")
    print("3. Update Marks")
    print("4. Delete Marks")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Insert Marks
    if choice == 1:
        mark = int(input("Enter student marks: "))
        marks.append(mark)
        print("Marks inserted successfully!")

    # Display Marks
    elif choice == 2:
        if len(marks) == 0:
            print("No marks available.")
        else:
            print("\nStudent Marks:")
            for i in range(len(marks)):
                print("Student", i + 1, ":", marks[i])

    # Update Marks
    elif choice == 3:
        if len(marks) == 0:
            print("No marks available to update.")
        else:
            student = int(input("Enter student number to update: "))

            if 1 <= student <= len(marks):
                new_mark = int(input("Enter new marks: "))
                marks[student - 1] = new_mark
                print("Marks updated successfully!")
            else:
                print("Invalid student number.")

    # Delete Marks
    elif choice == 4:
        if len(marks) == 0:
            print("No marks available to delete.")
        else:
            student = int(input("Enter student number to delete: "))

            if 1 <= student <= len(marks):
                marks.pop(student - 1)
                print("Marks deleted successfully!")
            else:
                print("Invalid student number.")

    # Exit
    elif choice == 5:
        print("Program ended.")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
