def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid!")

print("===================================== Mini Library System =====================================")

book_ids    = []
book_titles = []
available   = []

while True:
    print("\n1.Add Book  2.Issue Book  3.Return Book  4.Show All  5.Exit")
    choice = get_int("Choice: ")

    if choice == 1:
        bid   = get_int("Book ID: ")
        if bid in book_ids:
            print("ID exists!")
        else:
            title = input("Title: ").strip()
            book_ids.append(bid)
            book_titles.append(title)
            available.append(True)
            print("Book added!")

    elif choice == 2:
        bid = get_int("Book ID to issue: ")
        if bid in book_ids:
            idx = book_ids.index(bid)
            if available[idx]:
                available[idx] = False
                print(f"'{book_titles[idx]}' issued!")
            else:
                print("Already issued!")
        else:
            print("Not found!")

    elif choice == 3:
        bid = get_int("Book ID to return: ")
        if bid in book_ids:
            idx = book_ids.index(bid)
            if not available[idx]:
                available[idx] = True
                print(f"'{book_titles[idx]}' returned!")
            else:
                print("Was not issued!")
        else:
            print("Not found!")

    elif choice == 4:
        if not book_ids:
            print("No books!")
        else:
            for i in range(len(book_ids)):
                status = "Available" if available[i] else "Issued"
                print(f"ID: {book_ids[i]}  Title: {book_titles[i]}  [{status}]")

    elif choice == 5:
        print("Goodbye!")
        break