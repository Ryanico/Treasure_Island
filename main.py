print('''
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
# This is a welcome sign to Treasure Island.
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# This is the first prompt when you get to the Treasure Island.
choice1 = input('You come across a cross road. Which way do you think is the fastest and safest ? '
                'Type "right" or "left".').lower()
if choice1 == "left":
    choice2 = input('You come across a lake with two paths. Which one would you dare choose? '
                    'Type "swim" or "bridge"').lower()
    if choice2 == "bridge":
        choice3 = input('After crossing you come across a house with three doors. Which one would you dare open? '
              'Type "first" or "second" or "third" ').lower()
        if choice3 == "first":
            choice4 = input('Almost there. Three doors left Amigo! Which door is between you and a fortune of wealth +_-?. '
                  'Type "door1" or "door2" or "door3"').lower()
            if choice4 == "door3":
                print("Game over! An empty room HAHAHA! Sorry Amigo.")
            elif choice4 == "door2":
                print("Wow! There it is. You are rich Your Highness.")
            elif choice4 == "door1":
                print("Game over! A pirate eye patch. "
                      "At least you can boast to your friends at home you got to an island before them.")
        elif choice3 == "second":
            print("Game over! Got into a room full of venomous reptile and arachnids.")
        elif choice3 == "third":
            print("Game over! A one eyed ancient beast awaits to feast on you.")
    else:
        print("Game over! You got feasted by hungry Alligators")
else:
    print("Game over! You collided with pirates and killed you instantly")