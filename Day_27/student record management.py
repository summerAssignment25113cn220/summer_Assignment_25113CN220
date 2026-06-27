# Helper functions
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
            print("Invalid! This field cannot be empty.")
        elif any(char.isdigit() for char in value):
            print("Invalid! Please enter text only, no numbers.")
        else:
            return value

def get_year(prompt):
    valid = ["1", "2", "3", "4"]
    while True:
        value = input(prompt).strip()
        if value in valid:
            # Convert to "1st year", "2nd year" etc.
            suffix = {"1": "st", "2": "nd", "3": "rd", "4": "th"}
            return value + suffix[value] + " year"
        else:
            print("Invalid! Please enter 1, 2, 3 or 4 only.")

# ─────────────────────────────────────────
print("====================================== Student Record Management System ======================================")

students = []  # Stays alive as long as program runs

while True:
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. Search Student by Roll No.")
    print("3. Display All Students")
    print("4. Exit")

    choice = get_int("Enter choice: ")

    # ── ADD STUDENT ───────────────────────
    if choice == 1:
        print("\n--- Add Student ---")
        roll = get_int("Roll No.: ")

        # Check if roll no. already exists
        already_exists = False
        for s in students:
            if s["roll"] == roll:
                already_exists = True
                break

        if already_exists:
            print(f"Student with Roll No. {roll} already exists!")
        else:
            name   = get_string("Name: ")
            course = get_string("Course (example- BTech, BCA): ")
            branch = get_string("Branch (example- CSE, ECE): ")
            year   = get_year("Year (enter 1, 2, 3 or 4): ")

            students.append({
                "roll":   roll,
                "name":   name,
                "course": course,
                "branch": branch,
                "year":   year
            })
            print(f"Student '{name}' added successfully!")

    # ── SEARCH BY ROLL NO. ────────────────
    elif choice == 2:
        if len(students) == 0:
            print("No students added yet!")
        else:
            search_roll = get_int("Enter Roll No. to search: ")

            found = None
            for s in students:
                if s["roll"] == search_roll:
                    found = s
                    break

            if found:
                print("\n--- Student Details ---")
                print(f"Roll No. : {found['roll']}")
                print(f"Name     : {found['name']}")
                print(f"Course   : {found['course']}")
                print(f"Branch   : {found['branch']}")
                print(f"Year     : {found['year']}")
            else:
                print(f"No student found with Roll No. {search_roll}!")

    # ── DISPLAY ALL STUDENTS ──────────────
    elif choice == 3:
        if len(students) == 0:
            print("No students added yet!")
        else:
            print(f"\n--- All Students ({len(students)} total) ---")
            for s in students:
                print(f"Roll: {s['roll']}  Name: {s['name']}  "
                      f"Course: {s['course']}  Branch: {s['branch']}  "
                      f"Year: {s['year']}")

    # ── EXIT ──────────────────────────────
    elif choice == 4:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3 or 4.")