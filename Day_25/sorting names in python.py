n = int(input("Enter number of names: "))
names = []
for i in range(n):
    names.append(input(f"Enter name {i+1}: "))

names.sort()

print("Sorted names:")
for name in names:
    print(name)