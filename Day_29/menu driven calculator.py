def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid! Please enter a number.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid! Please enter a whole number.")

# ─────────────────────────────────────────
print("=== Menu-Driven Calculator ===")

while True:
    print("\n--- MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = get_int("Enter choice: ")

    if choice in [1, 2, 3, 4, 5, 6]:
        a = get_float("Enter first number: ")
        b = get_float("Enter second number: ")

        if choice == 1:
            print(f"Result = {a + b}")
        elif choice == 2:
            print(f"Result = {a - b}")
        elif choice == 3:
            print(f"Result = {a * b}")
        elif choice == 4:
            if b == 0:
                print("Error! Cannot divide by zero.")
            else:
                print(f"Result = {a / b}")
        elif choice == 5:
            print(f"Result = {a % b}")
        elif choice == 6:
            print(f"Result = {a ** b}")

    elif choice == 7:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")