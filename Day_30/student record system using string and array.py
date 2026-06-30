def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid! Whole numbers only.")

def get_cgpa(prompt):
    while True:
        val = get_int(prompt)
        if 0 <= val <= 10:
            return val
        print("Invalid! CGPA must be between 0 and 10.")

print("================================ Student Record System (Arrays & Strings) ================================")

rolls   = []
names   = []
courses = []
cgpas   = []
while True:
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. Search by Roll No.")
    print("3. Display All")
    print("4. Exit")
    choice = get_int("Enter choice: ")
    if choice == 1:
        roll = get_int("Roll No.: ")
        if roll in rolls:
            print("Roll No. already exists!")
        else:
            name   = input("Name: ").strip()
            course = input("Course: ").strip()
            cgpa   = get_cgpa("Cgpa (0-10): ")
            rolls.append(roll)
            names.append(name)
            courses.append(course)
            cgpas.append(cgpa)
            print("Student added!")
    elif choice == 2:
        roll = get_int("Enter Roll No.: ")
        if roll in rolls:
            idx = rolls.index(roll)
            print(f"\nRoll   : {rolls[idx]}")
            print(f"Name   : {names[idx]}")
            print(f"Course : {courses[idx]}")
            print(f"Cgpa   : {cgpas[idx]}")
            print(f"Result : {'PASS' if cgpas[idx] >= 4 else 'FAIL'}")
        else:
            print("Student not found!")
    elif choice == 3:
        if not rolls:
            print("No students added!")
        else:
            print(f"\n--- All Students ({len(rolls)} total) ---")
            for i in range(len(rolls)):
                print(f"Roll: {rolls[i]}  Name: {names[i]}  "
                      f"Course: {courses[i]}  Cgpa: {cgpas[i]}")
    elif choice == 4:
        print("Exiting!")
        break
    else:
        print("Invalid choice!")