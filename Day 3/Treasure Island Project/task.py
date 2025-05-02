print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Hunt.")
print("Your mission is to find the treasure.\n\n")
print("\n🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
print("Begin Your Journey from 🌲The Whispering Woods🌲\n")
print("You step into a forest where the trees seem to whisper ancient secrets. The path splits in two, and a wooden sign reads:")
print("Only one way leads to the truth. The other... to your doom.\n\n🗡️ Choose wisely, adventurer... " )
choice=input(("A) The foggy trail with glowing mushrooms – it pulses with quiet energy.\n"
              "B) The bright, cheerful path with singing birds – oddly silent as you step closer...\n Where you want to go(A or B): ")).upper()

if choice=="A":
    print("\n🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨")
    print("\n🎉Congratulations you survived in forest next is -🪨The Cursed Cliffs 🪨")
    print("\nAfter surviving the woods, you reach a cliff side with three cave entrances, each one darker than the last.\nA crow caws and flies away as you approach.")
    print("\nAbove the caves, a message is carved: Only those who see beyond light shall pass.")
    print("🚪 One path goes deeper. The others… never return...\n")
    choice = input(("A) Cave with faint glowing runes – almost invisible unless you're looking for them.\n"
                    "B) Cave echoing with beastly growls – something moves inside...\n"
                    "C) Cave covered in thick spider webs – you feel tiny eyes watching you.\n"
                    "Where you want to go(A or B or C): ")).upper()
    if choice=="A":
        print("\nSorry you fall from the Cliff💀")
    elif choice=="C":
        print("\nSorry you died 💀")
    else:
        print("\n🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊")
        print("\n🎉Congratulations you survived on Cliff next is -🌊The River of Echoes 🌊")
        print("\nDeep within the cave, you reach an underground river with two boats. A soft voice whispers...")
        print("\nRiches blind the greedy. The humble shall float.")
        print("💀 Pick the wrong one, and the water will never let go...\n")
        choice = input(("A) The old wooden boat tied beside a dim lantern – it's worn but steady.\n"
                        "B) The dazzling golden boat floating in the center – no oars, no anchor.\n"
                        "Where you want to go(A or B): ")).upper()
        if choice=="A":
            print("\nSorry you killed by Crocodile 💀")
        else:
            print("\n💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 💎 ")
            print("\n🎉Congratulations you survived on Water next is -🔐 Step 4: The Final Trial 🔐")
            print("You're now standing before two towering doors inside a chamber lit by blue flames.")
            print("Above them: One opens to glory. One to the abyss.")
            print("\n 💎 Open the right door… and the TREASURE IS YOURS!")
            print("\n ❌ Choose wrong… and you're trapped forever in darkness.\n")
            choice = input(("A) The door carved with a simple candle symbol – warm light flickers from within.\n"
                            "B) The door marked with a bleeding skull – it hums with a sinister pulse.\n"
                            "Where you want to go(A or B): ")).upper()
            if choice=="A":
                print("\nYou done it! The Treasure is Yours😎🍾")
            else:
                print("\n 💀You lost Forever in the Darkness of the Universe🌌")

else:
    print("\nSorry you lost in the forest 😞")


