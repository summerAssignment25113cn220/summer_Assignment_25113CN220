def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid! Please enter a whole number.")

# ─────────────────────────────────────────
print("=== Menu-Driven Array Operations ===")

arr = []

while True:
    print("\n--- MENU ---")
    print("1.  Add elements")
    print("2.  Display array")
    print("3.  Sum and Average")
    print("4.  Largest and Smallest")
    print("5.  Reverse array")
    print("6.  Sort ascending")
    print("7.  Sort descending")
    print("8.  Linear search")
    print("9.  Count even and odd")
    print("10. Exit")

    choice = get_int("Enter choice: ")

    if choice == 1:
        n = get_int("How many elements: ")
        arr = []
        for i in range(n):
            arr.append(get_int(f"Element {i+1}: "))
        print("Elements added!")

    elif choice == 2:
        if not arr: print("Array is empty!")
        else: print(f"Array: {arr}")

    elif choice == 3:
        if not arr: print("Array is empty!")
        else:
            total = sum(arr)
            print(f"Sum = {total}  Average = {total/len(arr):.2f}")

    elif choice == 4:
        if not arr: print("Array is empty!")
        else:
            print(f"Largest = {max(arr)}  Smallest = {min(arr)}")

    elif choice == 5:
        if not arr: print("Array is empty!")
        else:
            arr.reverse()
            print(f"Reversed: {arr}")

    elif choice == 6:
        if not arr: print("Array is empty!")
        else:
            arr.sort()
            print(f"Sorted ascending: {arr}")

    elif choice == 7:
        if not arr: print("Array is empty!")
        else:
            arr.sort(reverse=True)
            print(f"Sorted descending: {arr}")

    elif choice == 8:
        if not arr: print("Array is empty!")
        else:
            key = get_int("Enter element to search: ")
            if key in arr:
                print(f"Found at index {arr.index(key)}")
            else:
                print("Not found!")

    elif choice == 9:
        if not arr: print("Array is empty!")
        else:
            even = sum(1 for x in arr if x % 2 == 0)
            odd  = len(arr) - even
            print(f"Even count = {even}  Odd count = {odd}")

    elif choice == 10:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")