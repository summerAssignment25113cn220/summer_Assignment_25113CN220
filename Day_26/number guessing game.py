import random

print("=== Number Guessing Game ===")
secret = random.randint(1, 100)  # chooses random number between 1-100
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess < secret:
        print("Too Low! Try again.")
    elif guess > secret:
        print("Too High! Try again.")
    else:
        print(f"Correct! You got it in {attempts} attempts!") # f you puts variables directly inside {} 
        break