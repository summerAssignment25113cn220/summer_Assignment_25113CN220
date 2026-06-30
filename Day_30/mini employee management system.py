def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid!")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid!")

print("================================= Mini Employee Management System =================================")

emp_ids   = []
emp_names = []
emp_depts = []
emp_sals  = []

while True:
    print("\n1.Add  2.Search  3.Show All  4.Highest Paid  5.Exit")
    choice = get_int("Choice: ")

    if choice == 1:
        eid = get_int("ID: ")
        if eid in emp_ids:
            print("ID exists!")
        else:
            emp_ids.append(eid)
            emp_names.append(input("Name: ").strip())
            emp_depts.append(input("Dept: ").strip())
            emp_sals.append(get_float("Salary: "))
            print("Employee added!")

    elif choice == 2:
        eid = get_int("Enter ID: ")
        if eid in emp_ids:
            i = emp_ids.index(eid)
            print(f"ID: {emp_ids[i]}  Name: {emp_names[i]}  "
                  f"Dept: {emp_depts[i]}  Salary: Rs.{emp_sals[i]}")
        else:
            print("Not found!")

    elif choice == 3:
        if not emp_ids:
            print("No employees!")
        else:
            for i in range(len(emp_ids)):
                print(f"ID: {emp_ids[i]}  Name: {emp_names[i]}  "
                      f"Dept: {emp_depts[i]}  Sal: Rs.{emp_sals[i]}")

    elif choice == 4:
        if not emp_ids:
            print("No employees!")
        else:
            idx = emp_sals.index(max(emp_sals))
            print(f"Highest Paid: {emp_names[idx]} = Rs.{emp_sals[idx]}")

    elif choice == 5:
        print("Goodbye!")
        break