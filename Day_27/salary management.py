print("====================================== Salary Management System =======================================")

n = int(input("Enter number of employees: "))

employees = []

# Input and calculate salary
for i in range(n):
    print(f"\nEmployee {i+1}:")
    emp_id = int(input("ID: "))
    name   = input("Name: ")
    basic  = float(input("Basic Salary: "))

    # Calculate components
    hra        = 0.20 * basic   # 20% of basic
    da         = 0.10 * basic   # 10% of basic
    tax        = 0.10 * basic   # 10% of basic
    net_salary = basic + hra + da - tax

    employees.append({
        "id":     emp_id,
        "name":   name,
        "basic":  basic,
        "hra":    hra,
        "da":     da,
        "tax":    tax,
        "net":    net_salary
    })

# Display salary slips
print("\n--- Salary Slips ---")
for e in employees:
    print(f"\nID: {e['id']}  Name: {e['name']}")
    print(f"  Basic  : Rs. {e['basic']}")
    print(f"  HRA    : Rs. {e['hra']}")
    print(f"  DA     : Rs. {e['da']}")
    print(f"  Tax  - : Rs. {e['tax']}")
    print(f"  Net    : Rs. {e['net']}")