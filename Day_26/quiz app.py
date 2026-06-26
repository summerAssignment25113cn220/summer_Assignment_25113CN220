print("=== Quiz Application ===")

score = 0

# Question 1
print("\nQ1. What is 5 + 3?")
print("1) 6   2) 8   3) 9   4) 7")
ans = int(input("Answer: "))
if ans == 2:
    print("Correct!")
    score += 1
else:
    print("Wrong! Answer was 2 (8)")

# Question 2
print("\nQ2. What is the capital of India?")
print("1) Mumbai   2) Kolkata   3) Delhi   4) Chennai")
ans = int(input("Answer: "))
if ans == 3:
    print("Correct!")
    score += 1
else:
    print("Wrong! Answer was 3 (Delhi)")

# Question 3
print("\nQ3. How many days in a week?")
print("1) 5   2) 6   3) 8   4) 7")
ans = int(input("Answer: "))
if ans == 4:
    print("Correct!")
    score += 1
else:
    print("Wrong! Answer was 4 (7)")

# Result
print(f"\nYour Score: {score}/3")
if score == 3:
    print("Excellent!")
elif score >= 2:
    print("Good!")
else:
    print("Keep practicing!")