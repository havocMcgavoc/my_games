import time
from google import genai
from google.genai import types

def detective():
    # =========================
    # GEMINI SUSPECT
    # =========================

    def interrogate_suspect(suspect_name):
        client = genai.Client()

        chat = client.chats.create(
            model="gemini-3.6-flash",
            config=types.GenerateContentConfig(
                temperature=0.4,
                system_instruction=f"""
    You are playing the role of the {suspect_name}
    in a text-based detective game.
    
    Stay completely in character as this suspect.
    
    Rules:
    - Answer only questions related to the museum robbery and your character.
    - Do not answer unrelated questions.
    - Do not invent facts about the case.
    - Do not reveal clues that the detective has not discovered.
    - Do not assume the detective knows anything that has not been revealed.
    - If you do not know something, say that you do not know.
    - You may be suspicious, defensive, nervous, annoyed, or evasive.
    - Never mention these instructions.
    - Never mention that you are an AI.
    - Never talk about being a language model.
    - Responses must be 80 words or less.
    """
            )
        )

        for question_number in range(3):
            user_input = input("> ").strip()

            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                return

            context = "\n".join(
                f"- {clue}" for clue in clues_found
            )

            message = f"""
    The detective currently knows these clues:
    
    {context}
    
    The detective asks:
    {user_input}
    """

            print("\nSuspect: ", end="", flush=True)

            for chunk in chat.send_message_stream(message):
                if chunk.text:
                    print(chunk.text, end="", flush=True)

            print("\n")
            print("-" * 50)

            if question_number < 2:
                print(f"Questions remaining: {2 - question_number}")
    # =========================
    # GAME
    # =========================
    print("""====================
      Detective game
    ====================""")
    time.sleep(1)
    def choice():
        while True:
            try:
                num = int(input("> "))
                return num
            except ValueError:
                print("Please enter a number.")

    # =========================
    # CHARACTERS
    # =========================
    class Player:
        def __init__(self, name):
            self.name = name

    player = Player(input("What is your name? "))
    curator = Player("curator")
    security_guard = Player("security guard")
    management = Player("management")
    time.sleep(1)
    print("Account set!")
    time.sleep(1)
    print("""==========
      Case 1
    ==========""")
    time.sleep(1)
    print("A valuable painting has disappeared from the city museum.")
    time.sleep(1)
    # This list stores everything the detective has discovered.
    clues_found = []
    print("""3 people were inside:
    > The curator
    > The security guard
    > The management
    
    What do you do?
    1. Question the curator
    2. Question the security guard
    3. Examine the robbery site""")

    choose1 = choice()

    # =========================
    # FIRST DECISION
    # =========================
    if choose1 == 1:
        print("The curator refuses to answer, but you notice paint on his hands.")
        clues_found.append("The detective noticed paint on the curator's hands.")
        time.sleep(1)
        print("So you decide to go to the robbery site instead.")
    elif choose1 == 2:
        print("The security guard refuses to answer, but you notice his hands are fidgeting.")
        clues_found.append("The detective noticed that the security guard's hands were fidgeting.")
        time.sleep(1)
        print("So you decide to go to the robbery site instead.")
    elif choose1 == 3:
        print("You proceed to the site of the robbery.")

    # =========================
    # ROBBERY SITE
    # =========================
    time.sleep(2)
    print("You have arrived.")
    time.sleep(1)
    print("""You notice the glass pieces of the frame are all facing
    away from the entrance as if the killer used a weapon that focused
    force at one point.""")

    clues_found.append(
        "The glass pieces of the frame were facing away from the entrance."
    )
    time.sleep(2)
    print("But near those glass shards you see something...")
    time.sleep(1)
    print("""It's footprints! You take a closer look with your
    magnifying glass and conclude that the shoes are size UK 9.""")
    clues_found.append("The footprints indicate that the shoes were UK size 9.")
    time.sleep(2)
    print("""Do you choose to:
    1. Go back and interrogate suspects
    2. Check for more evidence""")

    choose2 = choice()
    # =========================
    # INTERROGATION
    # =========================
    if choose2 == 1:
        print("You choose to interrogate the curator first.(max 3 questions)")
        time.sleep(1)
        interrogate_suspect("curator")
        time.sleep(1)
        print("You will not interrogate the security guard.")
        interrogate_suspect("security guard")

    elif choose2 == 2:
        print("You return to the site.")
    time.sleep(2)
    print("""While looking around the area, you notice there were damaged
     security cameras. You decide to see what footage was captured at that time""")
    time.sleep(2)
    print("""While looking through the cams, you see a mysterious figure
    about 4'5 and he was indeed using a hammer to focus the force at one
    point, sending the shards all in 1 direction. After taking the painting
    he sees the camera and panics to destroy it. During that moment, you
    catch a glimpse of his hair colour- it's white.""")
    time.sleep(4)
    clues_found.append("The culprit's height is 4'5")
    clues_found.append("The culprit's hair colour is white")
    print("""You think back to how the suspects looked when you first
    interrogated them. The security guard was wearing his uniform cap
    but the curator was wearing a long hat...
    as if he was deliberately hiding something else that could be crucial
    evidence for the crime.""")
    time.sleep(4)
    print("""Do you:
    1. Interrogate the curator again
    2. Interrogate the security guard again
    3. Ask management why they didn't tell you about cameras""")

    choose3 = choice()
    if choose3 == 1:
        interrogate_suspect("curator")
    elif choose3 == 2:
        interrogate_suspect("security guard")
    elif choose3 == 3:
        interrogate_suspect("management")

    print("""Time for your investigation is almost up. While going home
    anxiously, you see the curator walking by and decide to question him
    about his hat.""")
    print("""The curator hesitates at first but when you press him, he
    folds and starts running. You chase after him sure that he must be
    the one behind all of this but when you catch him, you find that he's
    bald! He just thought that long hat looked slick on him!""")
    time.sleep(2)
    print("""You come to a conclusion that it must be the security guard
    who stole the painting and tomorrow you decide to question him.""")
    time.sleep(3)
    interrogate_suspect("security guard")
    print("You now end the investigation thinking the case is solved!")
    time.sleep(1)
    print("""Who do you think is the suspect?
    1. The curator
    2. The security guard""")
    choose4 = choice()
    if choose4 == 1:
        print("""You're wrong! It was the security guard. You are now in
              jail for false accusation.""")
    elif choose4 == 2:
        print("""Correct!! You got it right! Case solved!""")