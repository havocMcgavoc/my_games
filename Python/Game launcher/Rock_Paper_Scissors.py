import random
import time

def RockPaperScissors():
    def game():
        print("Welcome to Rock Paper Scissors! (Press e to exit)")
        user = input("""Enter your choice, Rock, Paper, or Scissors
        > """).lower().strip()
        choice = ["rock", "paper", "scissors"]
        computer = random.choice(choice)
        print(f"I chose {computer}")
        time.sleep(1)
        if (user == computer):
            print("It's a draw!")
        elif (user == "rock" and computer == "paper") or (user == "paper" and computer == "scissors") or (user == "scissors" and computer == "rock"):
            print("Yay! I win!")
        elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
            print("Aw man... you win.")

    game()
    attempt = input("Do you want to play again? (y/n)")
    while attempt == "y":
        game()
        attempt = input("Do you want to play again? (y/n)")
    if attempt == "n":
        print("Thank you for playing!")