# Helper functions to safely get input
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid! Please enter a whole number.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid! Please enter a number.")

def get_string(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Invalid! This field cannot be empty.")
        elif any(char.isdigit() for char in value):
            print("Invalid! Please enter text only, no numbers.")
        else:
            return value

# ─────────────────────────────────────────
print("=================================== Employee Management System ===================================")

employees = []  # Stays alive as long as program runs

while True:
    print("\n--- MENU ---")
    print("1. Add Employee")
    print("2. Search Employee by ID")
    print("3. Exit")

    choice = get_int("Enter choice: ")

    # ── ADD EMPLOYEE ──────────────────────
    if choice == 1:
        print("\n--- Add Employee ---")
        emp_id = get_int("ID: ")

        # Check if ID already exists
        already_exists = False
        for e in employees:
            if e["id"] == emp_id:
                already_exists = True
                break

        if already_exists:
            print(f"Employee with ID {emp_id} already exists!")
        else:
            name   = get_string("Name: ")
            dept   = get_string("Department: ")
            salary = get_float("Salary: ")

            employees.append({
                "id":     emp_id,
                "name":   name,
                "dept":   dept,
                "salary": salary
            })
            print(f"Employee '{name}' added successfully!")

    # ── SEARCH BY ID ──────────────────────
    elif choice == 2:
        if len(employees) == 0:
            print("No employees added yet!")
        else:
            search_id = get_int("Enter Employee ID to search: ")

            found = None
            for e in employees:
                if e["id"] == search_id:
                    found = e
                    break

            if found:
                print("\n--- Employee Details ---")
                print(f"ID         : {found['id']}")
                print(f"Name       : {found['name']}")
                print(f"Department : {found['dept']}")
                print(f"Salary     : Rs. {found['salary']}")
            else:
                print(f"No employee found with ID {search_id}!")

    # ── EXIT ──────────────────────────────
    elif choice == 3:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2 or 3.")