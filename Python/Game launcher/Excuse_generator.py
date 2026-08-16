import random
import time
import sounddevice as sd
import soundfile as sf

def excuse():
    print("Welcome to the Excuse Generator")
    time.sleep(1)
    prob = input("Enter your problem and I'll generate the perfect excuse for it.")
    time.sleep(1)
    print("Ok... that's one type of a problem")
    time.sleep(1)
    print(f"Analysing {prob}...")
    data, samplerate = sf.read("Elevator.wav")
    sd.play(data, samplerate)
    time.sleep(1)
    print(f"Looking for an excuse for {prob}...")
    thoughts = [
    "Consulting the potato database...",
    "Bribing the universe...",
    "Searching for someone else to blame...",
    "Deleting the CCTV footage...",
    "Asking my toaster for legal advice...",
    "Pretending to understand the situation..."
    ]
    subjects = [
        "My dog",
        "My toaster",
        "My potato",
        "My Arduino",
        "My goldfish",
        "A penguin",
        "The government",
        "An alien",
        "A raccoon",
        "A pigeon",
        "The FBI",
        "ChatGPT",
        "My calculator",
        "My Wi-Fi router",
        "My little brother",
        "A mosquito",
        "The moon"
    ]
    verb = [
        "ate",
        "deleted",
        "kaboomed",
        "stole",
        "launched",
        "evaporated",
        "confiscated",
        "drop-kicked",
        "accidentally sold",
        "microwaved",
        "yeeted"
    ]
    obj = [
        "my homework.",
        "the Wi-Fi.",
        "the school.",
        "the evidence.",
        "my exam paper.",
        "the moon.",
        "my dignity.",
        "my keyboard.",
        "the principal.",
        "my grades.",
        "the internet.",
        "my last braincell.",
        "the police car.",
        "my alarm clock.",
        "my lunch."
    ]
    time.sleep(1)

    for thoughts in random.sample(thoughts, 5): #The loading screen
        print(thoughts)
        time.sleep(1)

    print("Making something up...")
    for i in range(11): #The loading bar
        print(f"\r [{'█'*i}{' '*(10-i)}] {10 * i}%", end ="")
        time.sleep(1)
    sd.wait()

    print("\nYour excuse is done!")
    time.sleep(1)
    print(random.choice(subjects), random.choice(verb), random.choice(obj)) #The excuse
