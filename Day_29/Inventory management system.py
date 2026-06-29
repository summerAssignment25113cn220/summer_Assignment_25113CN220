def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid! Please enter a whole number.")

def get_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val < 0: print("Invalid! Cannot be negative.")
            else: return val
        except ValueError:
            print("Invalid! Please enter a number.")

def get_string(prompt):
    while True:
        value = input(prompt).strip()
        if value == "": print("Invalid! Cannot be empty.")
        else: return value

# ─────────────────────────────────────────
print("=== Inventory Management System ===")

inventory = []

while True:
    print("\n--- MENU ---")
    print("1. Add Item")
    print("2. Search Item by ID")
    print("3. Update Stock")
    print("4. Display All Items")
    print("5. Low Stock Alert (qty < 5)")
    print("6. Exit")

    choice = get_int("Enter choice: ")

    if choice == 1:
        item_id = get_int("Item ID: ")
        exists  = any(i["id"] == item_id for i in inventory)
        if exists:
            print("Item ID already exists!")
        else:
            name  = get_string("Item Name: ")
            price = get_float("Price: Rs. ")
            qty   = get_int("Quantity: ")
            inventory.append({"id": item_id, "name": name,
                               "price": price, "qty": qty})
            print(f"Item '{name}' added!")

    elif choice == 2:
        item_id = get_int("Enter Item ID: ")
        found   = next((i for i in inventory if i["id"] == item_id), None)
        if found:
            print(f"\nID    : {found['id']}")
            print(f"Name  : {found['name']}")
            print(f"Price : Rs. {found['price']}")
            print(f"Stock : {found['qty']} units")
        else:
            print("Item not found!")

    elif choice == 3:
        item_id = get_int("Enter Item ID: ")
        found   = next((i for i in inventory if i["id"] == item_id), None)
        if found:
            print(f"Current stock of '{found['name']}': {found['qty']}")
            print("1. Add stock   2. Remove stock")
            op  = get_int("Choice: ")
            qty = get_int("Quantity: ")
            if op == 1:
                found["qty"] += qty
                print(f"Stock updated! New qty: {found['qty']}")
            elif op == 2:
                if qty > found["qty"]:
                    print("Not enough stock!")
                else:
                    found["qty"] -= qty
                    print(f"Stock updated! New qty: {found['qty']}")
        else:
            print("Item not found!")

    elif choice == 4:
        if not inventory:
            print("No items in inventory!")
        else:
            print(f"\n--- Inventory ({len(inventory)} items) ---")
            for i in inventory:
                print(f"ID: {i['id']}  Name: {i['name']}  "
                      f"Price: Rs.{i['price']}  Qty: {i['qty']}")

    elif choice == 5:
        low = [i for i in inventory if i["qty"] < 5]
        if not low:
            print("All items have sufficient stock!")
        else:
            print("\n--- Low Stock Alert ---")
            for i in low:
                print(f"ID: {i['id']}  Name: {i['name']}  Qty: {i['qty']} ⚠️")

    elif choice == 6:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")