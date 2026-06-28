def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid! Please enter a whole number.")

def get_string(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Invalid! Cannot be empty.")
        else:
            return value

def get_phone(prompt):
    while True:
        phone = input(prompt).strip()
        if phone.isdigit() and len(phone) == 10:
            return phone
        print("Invalid! Enter a 10-digit phone number.")

# ─────────────────────────────────────────
print("=== Contact Management System ===")

contacts = []

while True:
    print("\n--- MENU ---")
    print("1. Add Contact")
    print("2. Search Contact by Name")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = get_int("Enter choice: ")

    if choice == 1:
        name  = get_string("Name: ")
        phone = get_phone("Phone (10 digits): ")
        email = get_string("Email: ")
        contacts.append({"name": name, "phone": phone, "email": email})
        print(f"Contact '{name}' added!")

    elif choice == 2:
        search = input("Enter name to search: ").strip().lower()
        found  = [c for c in contacts if search in c["name"].lower()]
        if found:
            print(f"\n--- Search Results ({len(found)} found) ---")
            for c in found:
                print(f"Name: {c['name']}  Phone: {c['phone']}  Email: {c['email']}")
        else:
            print("No contact found!")

    elif choice == 3:
        search = input("Enter name to update: ").strip().lower()
        found  = next((c for c in contacts if c["name"].lower() == search), None)
        if found:
            print(f"Current: {found['name']} | {found['phone']} | {found['email']}")
            found["phone"] = get_phone("New Phone: ")
            found["email"] = get_string("New Email: ")
            print("Contact updated!")
        else:
            print("Contact not found!")

    elif choice == 4:
        search = input("Enter name to delete: ").strip().lower()
        found  = next((c for c in contacts if c["name"].lower() == search), None)
        if found:
            contacts.remove(found)
            print(f"Contact '{found['name']}' deleted!")
        else:
            print("Contact not found!")

    elif choice == 5:
        if len(contacts) == 0:
            print("No contacts saved!")
        else:
            print(f"\n--- All Contacts ({len(contacts)} total) ---")
            for c in contacts:
                print(f"Name: {c['name']}  Phone: {c['phone']}  Email: {c['email']}")

    elif choice == 6:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")