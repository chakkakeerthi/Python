#------------------------------------------------------------------------------------------
#key componentes:
#1.word selection
#2.hangman art, blanks display
#3.player input and validation
#4.increment or hangman art display
#5.finalize the guessed word n display result
#------------------------------------------------------------------------------------------
import builtins  
import random
import time

def print(*args, **kwargs):
    builtins.print(*args, **kwargs)
    time.sleep(1.5)


def hangman_art(wrong_choice):
    art = {
        1: """   0
    
    
    
        """,
        2: """   
    0

    |    
    
    """,
        3: """   
    0

 /  |  

    """,
        4: """   
    0

 /  |  \\

    """,
        5: """   
    0

 /  |  \\

 /       """,
        6: """
    0

 /  |  \\
    
 /     \\ """,
    }

    return art[wrong_choice]


def hint(bot_word):
    hint_dict = {
        "Bear": "hibernates in winter",
        "Lion": "king of the jungle",
        "Wolf": "hunts in packs",
        "Deer": "has antlers",
        "Frog": "lives on land and water",
        "Goat": "provides milk",
        "Hare": "runs very fast",
        "Mole": "digs underground tunnels",
        "Mule": "known for strength",
        "Newt": "small amphibian",
        "Swan": "graceful swimming bird",
        "Wren": "tiny songbird",
        "Otter": "playful water mammal",
        "Panda": "eats bamboo",
        "Quail": "lays eggs",
        "Raven": "highly intelligent bird",
        "Shark": "ocean predator",
        "Sheep": "provides wool",
        "Skunk": "sprays strong odor",
        "Snail": "carries a shell",
        "Snake": "some species are venomous",
        "Tiger": "largest cat species",
        "Whale": "largest animal on Earth",
        "Zebra": "has black and white stripes",
        "Camel": "has humps",
        "Gecko": "climbs walls",
        "Hyena": "laugh-like call",
        "Lemur": "native to Madagascar",
        "Moose": "largest deer species",
        "Mouse": "small rodent",
        "Robin": "red-breasted bird",
        "Sloth": "moves slowly",
        "Squid": "has many arms",
        "Trout": "freshwater fish",
        "Bison": "large grazer",
        "Cobra": "spreads a hood",
        "Dingo": "wild Australian dog",
        "Eagle": "excellent eyesight",
        "Finch": "eats seeds",
        "Gator": "powerful jaws",
        "Heron": "long-legged bird",
        "Horse": "used for riding",
        "Koala": "eats eucalyptus leaves",
        "Llama": "used as a pack animal",
        "Macaw": "colorful parrot",
        "Okapi": "relative of giraffe",
        "Perch": "spiny-finned fish",
        "Tapir": "has a short trunk",
        "Tetra": "popular aquarium fish",
        "Viper": "venomous snake",
        "Badger": "burrowing mammal",
        "Beetle": "hard wing covers",
        "Bobcat": "short-tailed wild cat",
        "Caiman": "crocodile relative",
        "Cattle": "raised for milk and meat",
        "Donkey": "carries heavy loads",
        "Ferret": "playful pet",
        "Gerbil": "small pet rodent",
        "Grouse": "ground bird",
    }

    print(f"hint: {hint_dict[bot_word.capitalize()]}")


running = True
while running:

    choices = animals = [
        "Bear",
        "Lion",
        "Wolf",
        "Deer",
        "Frog",
        "Goat",
        "Hare",
        "Mole",
        "Mule",
        "Newt",
        "Swan",
        "Wren",
        "Otter",
        "Panda",
        "Quail",
        "Raven",
        "Shark",
        "Sheep",
        "Skunk",
        "Snail",
        "Snake",
        "Tiger",
        "Whale",
        "Zebra",
        "Camel",
        "Gecko",
        "Hyena",
        "Lemur",
        "Moose",
        "Mouse",
        "Robin",
        "Sloth",
        "Squid",
        "Trout",
        "Bison",
        "Cobra",
        "Dingo",
        "Eagle",
        "Finch",
        "Gator",
        "Heron",
        "Horse",
        "Koala",
        "Llama",
        "Macaw",
        "Okapi",
        "Perch",
        "Tapir",
        "Tetra",
        "Viper",
        "Badger",
        "Beetle",
        "Bobcat",
        "Caiman",
        "Cattle",
        "Donkey",
        "Ferret",
        "Gerbil",
        "Grouse",
    ]

    bot_word = random.choice(choices).lower()
    wrong_choice = 0
    word_length = ["_"] * len(bot_word)
    print(" ".join(word_length))

    while True:
        time.sleep(0.1)
        player_choice = input("\nenter your choice: ").lower()

        if (
            player_choice in bot_word
            and player_choice.isalpha()
            and len(player_choice) == 1
        ):
            for i in range(len(bot_word)):
                if bot_word[i] == player_choice:
                    word_length[i] = player_choice
            print(" ".join(word_length))

            if "_" not in word_length:
                print("you won the game!!")
                break

        elif (
            player_choice == " "
            or player_choice == ""
            or player_choice.isdigit()
            or len(player_choice) > 1
        ):
            print("enter a single letter at once!!")

        else:
            print("incorrect guess!!")
            wrong_choice += 1
            print(wrong_choice)
            print(hangman_art(wrong_choice))
            print(f"you have {6-wrong_choice} chances left!!")
            print(" ".join(word_length))

            if wrong_choice == 6:
                print("you lost the game!!")
                print(f"the word was {bot_word}")
                break

            if wrong_choice == 2:
                while True:
                    time.sleep(0.1)
                    player_input = input("wanna try a hint?? (y/n): ").lower()
                    if player_input == "y":
                        hint(bot_word)
                        break
                    elif player_input == "n":
                        break
                    else:
                        print("enter either y or n!!")

            if wrong_choice == 4:
                while True:
                    time.sleep(0.1)
                    player_input = input(
                        "wanna try another hint?? (y/n): "
                    ).lower()
                    if player_input == "y":
                        j = 2
                        for j in range(len(bot_word)):
                            if word_length[j] == "_":
                                word_length[j] = bot_word[j]
                                break
                        print(" ".join(word_length))
                        break
                    elif player_input == "n":
                        break
                    else:
                        print("enter either y or n!!")

    while True:
        time.sleep(0.1)
        replay = input("wanna play again?? (y/n): ").lower()
        if replay == "y":
            print("-----------------NEW GAME-----------------")
            break
        elif replay == "n":
            print("Thanks for playing!!")
            exit()
        else:
            print("enter either y or n!!")