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

# ─────────────────────────────────────────
print("=== Library Management System ===")

books = []  # Each book: id, title, author, available

while True:
    print("\n--- MENU ---")
    print("1. Add Book")
    print("2. Search Book by ID")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Exit")

    choice = get_int("Enter choice: ")

    if choice == 1:
        book_id = get_int("Book ID: ")
        exists  = any(b["id"] == book_id for b in books)
        if exists:
            print("Book ID already exists!")
        else:
            title  = get_string("Title: ")
            author = get_string("Author: ")
            books.append({"id": book_id, "title": title,
                          "author": author, "available": True})
            print(f"Book '{title}' added!")

    elif choice == 2:
        book_id = get_int("Enter Book ID: ")
        found   = next((b for b in books if b["id"] == book_id), None)
        if found:
            status = "Available" if found["available"] else "Issued"
            print(f"\nID: {found['id']}  Title: {found['title']}  "
                  f"Author: {found['author']}  Status: {status}")
        else:
            print("Book not found!")

    elif choice == 3:
        book_id = get_int("Enter Book ID to issue: ")
        found   = next((b for b in books if b["id"] == book_id), None)
        if found:
            if found["available"]:
                found["available"] = False
                print(f"Book '{found['title']}' issued successfully!")
            else:
                print("Book is already issued!")
        else:
            print("Book not found!")

    elif choice == 4:
        book_id = get_int("Enter Book ID to return: ")
        found   = next((b for b in books if b["id"] == book_id), None)
        if found:
            if not found["available"]:
                found["available"] = True
                print(f"Book '{found['title']}' returned successfully!")
            else:
                print("Book was not issued!")
        else:
            print("Book not found!")

    elif choice == 5:
        if len(books) == 0:
            print("No books added yet!")
        else:
            print(f"\n--- All Books ({len(books)} total) ---")
            for b in books:
                status = "Available" if b["available"] else "Issued"
                print(f"ID: {b['id']}  Title: {b['title']}  "
                      f"Author: {b['author']}  [{status}]")

    elif choice == 6:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")