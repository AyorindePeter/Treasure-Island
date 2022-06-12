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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island, Find the treasure of get kikced out of the Island !!!")
left = input('You are at a Junction,Press "L" to move left and "R" to move right. Be Careful, a wrong turn and you are out of the island \n').upper()
if left == "L":
    wait = input('You are at the mouth of a river would you rather swim or wait for a boat. Type "S" to swim or "W" to wait for a boat \n').upper()
    if wait == 'W':
        door = input("""You are in front of a Yellow, Blue and Red Door. To enter the Yellow door, Type 'Y'
        To enter the blue door, type'B'
        To enter a red door, Type 'R' \n """).upper()

        if door == "Y":
            print('You have found the treasure, you win.')
        elif door == "R":
            print('You just entered into a furnace and you were burnt. Game Over!')
        elif door == "B":
            print("You entered into a Lion's den and eaten by the Lion. Game Over!")
        else:
            print("You didn't enter any of the provided doors and was washed away by a great flood. Game over")

    else:
        print('You were attacked by a crocodile, Game Over')


else:
    print('You took a wrong turn, you have to leave the island immediately')
