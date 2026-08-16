import random

def guess():
    print("Welcome to the Number Guessing Game!")
    difficulty = input("""Which level of difficulty do you want?
    1. Easy: 1-20
    2. Medium: 1-50
    3. Hard: 1-100
    >>> """).lower().strip()
    if difficulty == "1" or difficulty == "easy":
        number = random.randint(1, 20)
    elif difficulty == "2" or difficulty == "medium":
        number = random.randint(1, 50)
    elif difficulty == "3" or difficulty == "hard":
        number = random.randint(1, 100)

    attempt = 1
    guess = int(input("What is your guess:"))
    print(f"Attempt: {attempt}")
    if guess != number:
        attempt += 1
    while guess != number:
        if abs(guess - number) == 1:
            print("You're off by just 1!")
            print(f"Attempt: {attempt}")
            attempt += 1
            guess = int(input("Try again: "))
        elif abs(guess - number) <= 5:
            print("You're really close!")
            print(f"Attempt: {attempt}")
            attempt += 1
            guess = int(input("Try again: "))
        elif abs(guess - number) <= 10:
            print("You're getting there")
            print(f"Attempt: {attempt}")
            attempt += 1
            guess = int(input("Try again: "))
        elif abs(guess - number) <= 15:
            print("You're a little off.")
            print(f"Attempt: {attempt}")
            attempt += 1
            guess = int(input("Try again: "))
        elif abs(guess - number) >= 16:
            print("You're a way off.")
            print(f"Attempt: {attempt}")
            attempt += 1
            guess = int(input("Try again: "))
    if guess == number:
        print(f"Congratulations! You guessed the number in {attempt - 1} attempts!")