def sanitize_name(first_name, last_name):
    
    first_name = first_name.strip()
    last_name = last_name.strip()

    
    first_name = first_name.title()
    last_name = last_name.title()

    return f"{first_name} {last_name}"


first = input("Enter first name: ")
last = input("Enter last name: ")

full_name = sanitize_name(first, last)
print("Clean name:", full_name)