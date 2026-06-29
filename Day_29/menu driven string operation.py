def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid! Please enter a whole number.")

# ─────────────────────────────────────────
print("=== Menu-Driven String Operations ===")

while True:
    s = input("\nEnter a string (or 'exit' to quit): ").strip()
    if s.lower() == "exit":
        print("Exiting... Goodbye!")
        break

    print("\n--- MENU ---")
    print("1. Length of string")
    print("2. Reverse string")
    print("3. Uppercase")
    print("4. Lowercase")
    print("5. Count vowels and consonants")
    print("6. Check palindrome")
    print("7. Count words")
    print("8. Remove spaces")
    print("9. Character frequency")

    choice = get_int("Enter choice: ")

    if choice == 1:
        print(f"Length = {len(s)}")

    elif choice == 2:
        print(f"Reversed = {s[::-1]}")

    elif choice == 3:
        print(f"Uppercase = {s.upper()}")

    elif choice == 4:
        print(f"Lowercase = {s.lower()}")

    elif choice == 5:
        vowels = sum(1 for c in s.lower() if c in "aeiou")
        conson = sum(1 for c in s.lower() if c.isalpha() and c not in "aeiou")
        print(f"Vowels = {vowels}  Consonants = {conson}")

    elif choice == 6:
        clean = s.lower().replace(" ", "")
        if clean == clean[::-1]:
            print("Palindrome!")
        else:
            print("Not a palindrome.")

    elif choice == 7:
        print(f"Word count = {len(s.split())}")

    elif choice == 8:
        print(f"Without spaces = {s.replace(' ', '')}")

    elif choice == 9:
        ch = input("Enter character: ").strip()
        print(f"'{ch}' appears {s.count(ch)} times")

    else:
        print("Invalid choice!")