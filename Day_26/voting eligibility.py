print("=== Voting Eligibility System ===")

name    = input("Enter your name: ")
age     = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18 and citizen == "yes":
    print(f"{name}, you are ELIGIBLE to vote!")
elif age < 18:
    print(f"{name}, you are NOT eligible. You must be 18+")
else:
    print(f"{name}, you are NOT eligible. Must be a citizen.")