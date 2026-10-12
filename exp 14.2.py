def phonebook_app():
    # Dictionary to store names and contact numbers
    phonebook = {}
    
    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            name = input("Enter contact name: ").strip()
            
            # Check for existing listing to prevent overwrites
            if name in phonebook:
                print(f"Error: '{name}' already exists with number {phonebook[name]}. Cannot overwrite.")
            else:
                number = input("Enter contact phone number: ").strip()
                phonebook[name] = number
                print(f"Success: Contact '{name}' added successfully.")
                
        elif choice == '2':
            # Display the complete directory
            print("\n--- Complete Phonebook Directory ---")
            if not phonebook:
                print("The phonebook is currently empty.")
            else:
                for name, number in sorted(phonebook.items()):
                    print(f"Name: {name} | Phone: {number}")
                    
        elif choice == '3':
            print("Exiting Phonebook application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option from the menu.")

# Run the phonebook application
phonebook_app()