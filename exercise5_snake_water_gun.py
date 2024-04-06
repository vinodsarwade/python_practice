'''Question- 
Snake water and gun are the variation of the childrens game.when players use hand geusture to represent a snake,water or gun
the gun beats the snake,the water beats the gun and snake beats the water.
write a python program to create this game using if-else.'''

import random 

computer_input = random.randint(0,2)   #it will generate randon number between 0 to 2
user_input = int(input("0 for snake, 1 for water and 2 for gun\n"))

def check(computer_input,user_input):
    if (computer_input == user_input):
        return 0
    if(computer_input == 0 and user_input == 1):
        return -1
    if(computer_input == 1 and user_input == 2):
        return -1
    if(computer_input == 2 and user_input == 0):
        return -1
    return 1

score= check(computer_input, user_input)
if (score == 0):
    print("it's a draw")
elif(score == -1):
    print("you loose")
else:
    print("you win")
