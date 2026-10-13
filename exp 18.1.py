thought = input("Enter your thoughts: ")

with open("diary.txt", "a") as file:
    file.write(thought + "\n\n")

print("Thoughts saved successfully!")