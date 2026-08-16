import random
import time
import sounddevice as sd
import soundfile as sf

def magic_ball():
    print("Welcome to the Magic 8 Ball Game")
    user = input("""Enter any question and I will answer it.
    > """)
    thoughts = [
        "Consulting the potato database...",
        "Bribing the universe...",
        "Asking my toaster for legal advice...",
        "Pretending to understand the situation...",
        "Installing wisdom..."
    ]
    data, samplerate = sf.read("hall-of-the-mountain-king.wav")
    sd.play(data, samplerate)
    for thought in random.sample(thoughts, 4):
        print(thought)
        time.sleep(1)

    for i in range(11):
        print(f"\r[{'█'*i}{' '*(10-i)}] {10*i}% complete", end="")
        time.sleep(1)
    sd.wait()
    answers = ["yes", "no", "maybe", "god won't let me tell you this."]
    time.sleep(1)
    print(f"\n{random.choice(answers)}")
    time.sleep(0.5)
    print("Probably... Terms and Conditions apply.")