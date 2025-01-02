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

# Start the game loop
while True:
    # First decision: Crossroad
    option1 = input('You are at a cross road. Where do you want to go?\n    Type "left" or "right"\n').lower()
    if option1 == 'left':
        print("You've come to a lake. There is an island in the middle of the lake.")
        while True:
            # Second decision: swim or wait
            option2 = input('    Type "swim" to swim across. Type "wait" to wait for a boat.\n').lower()
            if option2 == 'wait':
                while True:
                    print("You arrived at the island unharmed. There is a house with three doors.")
                    # Third decision: Choose a door
                    option3 = input("    One red, one yellow, and one blue. Which color do you choose?\n").lower()
                    if option3 == 'yellow':
                        print("You find the treasure! You win.")
                        exit()
                    elif option3 == 'red':
                        print("You enter a room in fire. Game over.")
                        exit()
                    elif option3 == 'blue':
                        print("You enter a room full of beasts. Game over.")
                        exit()
                    else:
                        print("Please type a valid choice")
                        exit()
            elif option2 == 'swim':
                print("You got attacked by a crocodile. Game over.")
                exit()
            else:
                print("Please type in a valid choice.")
    elif option1 == 'right':
        print("You fail into a hole. Game over.")
        exit()
    else:
        print("Please type in a valid choice.")