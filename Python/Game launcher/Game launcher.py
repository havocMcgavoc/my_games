import Excuse_generator as Excuse
import Magic_8_ball as Mb
import Number_Guessing_Game as Guess
import Rock_Paper_Scissors as rps
import Hangman
import Detective_game as Dg
import Polygon_maker as pm

print("""============================== Game launcher ==============================""")


def launch_game():
    print("""
 1. Excuse generator
 2. Magic 8 ball
 3. Number Guessing Game
 4. Rock Paper Scissors
 5. Hangman
 6. Detective game
 7. Polygon maker""")

    while True:
        try:
            game = int(input("Which game would you like to play? (Enter number only): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if game == 1:
        Excuse.excuse()
    elif game == 2:
        Mb.magic_ball()
    elif game == 3:
        Guess.game()
    elif game == 4:
        rps.RockPaperScissors()
    elif game == 5:
        Hangman.hangman()
    elif game == 6:
        Dg.detective()
    elif game == 7:
        pm.polygon()
    else:
        print("Invalid choice. Please choose a number between 1 and 7.")


# --- Main Program Control Loop ---
while True:
    launch_game()

    # Prompt the user and cleanly evaluate their response
    play_again = input("\nWould you like to play another game? (y/n): ").lower().strip()
    if play_again != "y":
        print("Thank you for playing!")
        break
