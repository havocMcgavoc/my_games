import Excuse_generator as Excuse
import Magic_8_ball as Mb
import Number_Guessing_Game as Guess
import Rock_Paper_Scissors as rps
import Hangman
import Detective_game as Dg

print("""==============================
        Game launcher
==============================""")

def hub():
    print("""
1. Excuse generator
2. Magic 8 ball
3. Number Guessing Game
4. Rock Paper Scissors
5. Hangman
6. Detective game""")

    while True:
        try:
            game = int(input("Which game would you like to play?(Enter number only) "))
            break
        except ValueError:
            print("Please enter a number")
    if game == 1:
        Excuse.excuse()
    elif game == 2:
        Mb.magic_ball()
    elif game == 3:
        Guess.guess()
    elif game == 4:
        rps.RockPaperScissors()
    elif game == 5:
        Hangman.hangman()
    elif game == 6:
        Dg.detective()

hub()
attempt = input("Would you like to play another game? (y/n)").lower().strip()
while attempt == "y":
    hub()
    attempt = input("Would you like to play another game? (y/n)").lower().strip()
else:
    print("Thank you for playing")