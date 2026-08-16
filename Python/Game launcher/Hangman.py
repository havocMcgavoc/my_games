import random

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
    display = ["_"] * len(word)
    print(" ".join(display))
    print("\n")
    guess = input("What's the letter?: ").lower().strip()
    while "_" in display:
        if guess not in word:
            print("\r"+" ".join(display))
            if "_" not in display:
                print("You completed the word!")
                break
            guess = input("\rWrong! What's the next letter?: ").lower().strip()
        else:
            for i in range(len(word)):
                if guess == word[i]:
                    display[i] = guess
                    print("\r"+" ".join(display))
                    if "_" not in display:
                        print("You completed the word!")
                        break
                    guess = input("\rCorrect! What's the next letter?: ").lower().strip()
