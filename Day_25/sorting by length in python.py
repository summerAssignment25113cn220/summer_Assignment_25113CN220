n = int(input("Enter number of words: "))
words = []
for i in range(n):
    words.append(input(f"Enter word {i+1}: "))

words.sort(key=len)

print("Words sorted by length:")
for word in words:
    print(word)