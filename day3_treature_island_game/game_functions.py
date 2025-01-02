def treature_island_game():
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
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    crossroad()


def crossroad():
    """Handle the first decision at the crossroad."""
    choice = input('You are at a cross road. Where do you want to go?\nType "left" or "right": \n').lower()
    if choice == "left":
        lake()
    elif choice == "right":
        print("You fall into a hole. Game over.")
    else:
        print("Invalid choice. Please type in 'left' or 'right'.")
        crossroad()

def lake():
    """Handle the second decision at the lake."""
    choice = input('    Type "swim" to swim across. Type "wait" to wait for a boat.\n').lower()
    if choice == "wait":
        doors()
    elif choice == "swim":
        print("You got attacked by a crocodile. Game over.")
    else:
        print("Invalid choice. Please type in 'wait' or 'swim'.")
        lake()

def doors():
    print("You arrived at the island unharmed. There is a house with three doors.")
    choice = input("    One red, one yellow, and one blue. Which color do you choose?\n").lower()
    if choice == "yellow":
        print("You find the treasure! You win.")
    elif choice == "red":
        print("You enter a room in fire. Game over.")
    elif choice == "blue":
        print("You enter a room full of beasts. Game over.")
    else:
        print("Invalid choice. Please type in 'red', 'yellow', or 'blue'.")
        doors()


if __name__ == "__main__":
    treature_island_game()
