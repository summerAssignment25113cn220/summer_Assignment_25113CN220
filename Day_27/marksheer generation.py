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
        elif any(char.isdigit() for char in value):
            print("Invalid! Text only, no numbers.")
        else:
            return value

def get_marks(subject):
    while True:
        marks = get_int(f"Marks in {subject} (0-100): ")
        if 0 <= marks <= 100:
            return marks
        print("Invalid! Marks must be between 0 and 100.")

def get_grade(avg):
    if avg >= 90:   return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    elif avg >= 40: return "D"
    else:           return "F"

# ─────────────────────────────────────────
print("=== Marksheet Generation System ===")

students   = []
subjects   = ["Maths", "Physics", "Chemistry", "English", "CS"]

while True:
    print("\n--- MENU ---")
    print("1. Add Student Marks")
    print("2. Generate Marksheet by Roll No.")
    print("3. Display All Marksheets")
    print("4. Exit")

    choice = get_int("Enter choice: ")

    if choice == 1:
        print("\n--- Add Student ---")
        roll = get_int("Roll No.: ")

        already_exists = False
        for s in students:
            if s["roll"] == roll:
                already_exists = True
                break
        if already_exists:
            print(f"Roll No. {roll} already exists!")
            continue

        name   = get_string("Name: ")
        marks  = {}
        for sub in subjects:
            marks[sub] = get_marks(sub)

        total  = sum(marks.values())
        avg    = total / len(subjects)
        grade  = get_grade(avg)
        result = "PASS" if avg >= 40 else "FAIL"

        students.append({
            "roll":   roll,
            "name":   name,
            "marks":  marks,
            "total":  total,
            "avg":    avg,
            "grade":  grade,
            "result": result
        })
        print(f"Marksheet for '{name}' saved!")

    elif choice == 2:
        if len(students) == 0:
            print("No students added yet!")
            continue

        roll = get_int("Enter Roll No.: ")
        found = None
        for s in students:
            if s["roll"] == roll:
                found = s
                break

        if found:
            print(f"\n{'='*35}")
            print(f"        MARKSHEET")
            print(f"{'='*35}")
            print(f"Roll No. : {found['roll']}")
            print(f"Name     : {found['name']}")
            print(f"{'-'*35}")
            for sub, mark in found["marks"].items():
                print(f"{sub:<12}: {mark}/100")
            print(f"{'-'*35}")
            print(f"Total    : {found['total']}/{len(subjects)*100}")
            print(f"Average  : {found['avg']:.2f}%")
            print(f"Grade    : {found['grade']}")
            print(f"Result   : {found['result']}")
            print(f"{'='*35}")
        else:
            print(f"No student found with Roll No. {roll}!")

    elif choice == 3:
        if len(students) == 0:
            print("No students added yet!")
        else:
            print(f"\n--- All Marksheets ({len(students)} students) ---")
            for s in students:
                print(f"Roll: {s['roll']}  Name: {s['name']}  "
                      f"Total: {s['total']}  Avg: {s['avg']:.2f}%  "
                      f"Grade: {s['grade']}  [{s['result']}]")

    elif choice == 4:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")