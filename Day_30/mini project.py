def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid! Whole number only.")
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid! Number only.")
def get_string(prompt):
    while True:
        value = input(prompt).strip()
        if value == "": print("Cannot be empty!")
        else: return value
def get_grade(avg):
    if avg >= 90:   return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    elif avg >= 40: return "D"
    else:           return "F"
def add_student(students):
    roll = get_int("Roll No.: ")
    if any(s["roll"] == roll for s in students):
        print("Roll already exists!")
        return
    name   = get_string("Name: ")
    course = get_string("Course: ")
    marks  = get_float("Marks (0-100): ")
    grade  = get_grade(marks)
    students.append({"roll": roll, "name": name,
                     "course": course, "marks": marks, "grade": grade})
    print(f"Student '{name}' added! Grade: {grade}")
def search_student(students):
    roll  = get_int("Enter Roll No.: ")
    found = next((s for s in students if s["roll"] == roll), None)
    if found:
        print(f"\nRoll   : {found['roll']}")
        print(f"Name   : {found['name']}")
        print(f"Course : {found['course']}")
        print(f"Marks  : {found['marks']}")
        print(f"Grade  : {found['grade']}")
        print(f"Result : {'PASS' if found['marks'] >= 40 else 'FAIL'}")
    else:
        print("Student not found!")
def show_all(students):
    if not students:
        print("No students added!")
        return
    print(f"\n--- All Students ({len(students)} total) ---")
    for s in students:
        print(f"Roll: {s['roll']}  Name: {s['name']}  "
              f"Marks: {s['marks']}  Grade: {s['grade']}")
def show_branch_count(students):
    if not students:
        print("No students!")
        return
    branch_count = {}
    for s in students:
        course = s["course"]
        branch_count[course] = branch_count.get(course, 0) + 1
    print(f"\n--- Student Count by Branch ---")
    for course, count in branch_count.items():
        print(f"{course}: {count} student(s)")
# ─────────────────────────────────────────
print("============================== Complete Student Management System ================================")
students = []
while True:
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Show All Students")
    print("4. Show Branch-wise Count")
    print("5. Exit")
    choice = get_int("Enter choice: ")
    if   choice == 1: add_student(students)
    elif choice == 2: search_student(students)
    elif choice == 3: show_all(students)
    elif choice == 4: show_branch_count(students)
    elif choice == 5: print("Goodbye!"); break
    else: print("Invalid choice!")