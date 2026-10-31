import random
import sys

def hangman():
    print("Welcome to hangman!")
    words = [
        "velociraptor",
        "lantern",
        "pickle",
        "nebula",
        "thunder",
        "accordion",
        "marmalade",
        "quicksand",
        "telescope",
        "cactus",
        "moonlight",
        "sardine",
        "avalanche",
        "whistle",
        "goblin",
        "cinnamon",
        "submarine",
        "jellyfish",
        "paradox",
        "breadcrumb",
        "volcano",
        "kazoo",
        "pigeon",
        "midnight",
        "waffle",
        "labyrinth",
        "turnip",
        "comet",
        "backpack",
        "squirrel",
        "origami",
        "thunderbolt",
        "noodle",
        "fortress",
        "hamster",
        "eclipse",
        "stapler",
        "dragonfly",
        "microwave",
        "skeleton",
        "marshmallow",
        "compass",
        "pineapple",
        "broomstick",
        "hedgehog",
        "cathedral",
        "pancake",
        "meteorite",
        "shoelace",
        "flibbertigibbet",
        "toaster",
        "zeppelin",
        "cucumber",
        "bureaucracy",
        "cryptid"
    ]
    word = random.choice(words)
    print("I have thought of a word and you must guess it")
    attempt = 10
    display = ["_"] * len(word)
    print(" ".join(display))
    print()
    guess = input("What's the letter?: ").lower().strip()
    while "_" in display:
        if guess not in word:
            print("\r"+" ".join(display))
            if "_" not in display:
                print(f"You completed the word! You got it in {attempt} attempts!")
                break
            attempt -= 1
            guess = input(f"""\rWrong! What's the next letter?
You have {attempt} attempts left.
>""").lower().strip()
            if attempt == 1:
                print("You lost...")
                sys.exit()
        else:
            for i in range(len(word)):
                if guess == word[i]:
                    display[i] = guess
                    print("\r"+" ".join(display))
                    if "_" not in display:
                        print("You completed the word!")
                        break
                    guess = input(f"""\rCorrect! What's the next letter?
You have {attempt} attempts left.
>""").lower().strip()