from os import system
from time import sleep
from random import randint

'''class moves():
    def __init__(self):
        first_form = {"Damage":10, "Stamina":30}
        second_form = {"Damage":30, "Stamina":60}
        third_form = {"Damage":60, "Stamina":150}'''

def print_board():
    system("cls")
    print("Bot Health: " + str(bot["Health"]) + "\n")
    print("     Move        Damage      Stamina")
    print("1| First Form      10           30  ")
    print("2| Second Form     30           60  ")
    print("3| Third Form      60           150 ")
    print("\nHealth: " + str(user["Health"]))
    print("Stamina: " + str(user["Stamina"]))

def user_move():
    while True:
        move = input("Your move: ")
        if move == "1":
            bot["Health"] -= 10
            user["Stamina"] -=30
            return
        elif move == "2":
            bot["Health"] -= 30
            user["Stamina"] -= 60
            return
        elif move == "3":
            bot["Health"] -= 60
            user["Stamina"] -=150
            return

def bot_move():
    move = randint(1,3)
    if move == 1:
        user["Health"] -= 10
        return
    elif move == 2:
        user["Health"] -= 30
        return
    elif move == 3:
        user["Health"] -= 60
        return


system("cls")
print("I see you want to fight me...")

user = {"Health":100, "Stamina":200,"Form":"Water"}
bot = {"Health":100, "Difficulty":None}

while user["Health"] > 0 and bot["Health"] > 0:
    print_board()
    user_move()
    system("cls")
    print("Ouch!")
    sleep(1)
    print("Take this!")
    sleep(1)
    bot_move()

print("Game Over!")

