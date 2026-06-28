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
            if val <= 0:
                print("Invalid! Amount must be greater than 0.")
            else:
                return val
        except ValueError:
            print("Invalid! Please enter a number.")

def get_string(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Invalid! Cannot be empty.")
        elif any(char.isdigit() for char in value):
            print("Invalid! Text only.")
        else:
            return value

# ─────────────────────────────────────────
print("=== Bank Account System ===")

accounts = []

while True:
    print("\n--- MENU ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Mini Statement (last 5 transactions)")
    print("6. Exit")

    choice = get_int("Enter choice: ")

    if choice == 1:
        acc_no = get_int("Account No.: ")
        exists = any(a["acc_no"] == acc_no for a in accounts)
        if exists:
            print("Account already exists!")
        else:
            name    = get_string("Name: ")
            balance = get_float("Initial deposit: Rs. ")
            accounts.append({
                "acc_no":       acc_no,
                "name":         name,
                "balance":      balance,
                "transactions": [f"Account opened with Rs.{balance}"]
            })
            print(f"Account created! Account No.: {acc_no}")

    elif choice in [2, 3, 4, 5]:
        acc_no = get_int("Enter Account No.: ")
        acc    = next((a for a in accounts if a["acc_no"] == acc_no), None)

        if not acc:
            print("Account not found!")
            continue

        if choice == 2:
            amt = get_float("Enter deposit amount: Rs. ")
            acc["balance"] += amt
            acc["transactions"].append(f"Deposited Rs.{amt}  Balance: Rs.{acc['balance']}")
            print(f"Deposited! New balance = Rs. {acc['balance']}")

        elif choice == 3:
            amt = get_float("Enter withdrawal amount: Rs. ")
            if amt > acc["balance"]:
                print("Insufficient balance!")
            else:
                acc["balance"] -= amt
                acc["transactions"].append(f"Withdrew  Rs.{amt}  Balance: Rs.{acc['balance']}")
                print(f"Withdrawn! New balance = Rs. {acc['balance']}")

        elif choice == 4:
            print(f"\nAccount No. : {acc['acc_no']}")
            print(f"Name        : {acc['name']}")
            print(f"Balance     : Rs. {acc['balance']}")

        elif choice == 5:
            print(f"\n--- Last 5 Transactions for {acc['name']} ---")
            last5 = acc["transactions"][-5:]
            for t in last5:
                print(f"  {t}")

    elif choice == 6:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")