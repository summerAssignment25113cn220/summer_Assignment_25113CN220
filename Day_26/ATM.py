print("=== ATM Simulation ===")

pin     = 1234
balance = 10000.0

entered_pin = int(input("Enter PIN: "))

if entered_pin != pin:
    print("Wrong PIN! Access Denied.")
else:
    print("PIN Correct! Welcome.")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print(f"Balance = Rs. {balance}")    # f you puts variables directly inside {}

        elif choice == 2:
            amt = float(input("Enter amount to deposit: "))
            balance += amt
            print(f"Deposited! New balance = Rs. {balance}")

        elif choice == 3:
            amt = float(input("Enter amount to withdraw: "))
            if amt > balance:
                print("Insufficient balance!")
            else:
                balance -= amt
                print(f"Withdrawn! New balance = Rs. {balance}")

        elif choice == 4:
            print("Thank you! Goodbye.")
            break

        else:
            print("Invalid choice!")