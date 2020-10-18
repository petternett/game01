import sys 
# generate random integer values
from random import randint

#global variables
x = y = None
mesg = None

#game start
def start():
    x == 0
    y == 0
    print("\nWelcome to the game!\n")
    generate_hole()

#objects
    #holes
def generate_hole():
    holeX = randint(-1, 1)
    holeY = randint(-1, 1)
    game(holeX, holeY)

#leveling


#the game

def game(hX, hY):
    x = y = 0
    level = 1
    cur_holeX = hX
    cur_holeY = hY
    global mesg;

    while True:
        # Draw level

        move = input("Where do you want to move? up/down/left/right? \n")
        if move.lower() == "up":
            y += 1
        elif move.lower() == "down":
            y -= 1
        elif move.lower() == "left":
            x -= 1
        elif move.lower() == "right":
            x += 1
        else:
            print("\nInvalid move, please try again..\n")
            continue

        #check if edge
        if (x >= 2 or x <= -2 or y >= 2 or y <= -2):
            game_end_lose("Oh no. You fell over the edge..\n")

        #check for holes
        if (cur_holeX == x and cur_holeY == y):
            level += 1
            print(f"\nYou found the hole! You are now on level {level}\n")
            x == 0
            y == 0

        #check for win
        if level >= 10:
            game_end_win()

        #print if move was valid
        print(f"\nYou moved {move.lower()}. New position is {x}x, {y}y.")

#restart
def restart():
    while True:
        restart = input("\nDo you want to restart ? (Y/N) \n")
        if restart.upper() == "Y":
            print("\nRestarting game...\n\n\n")
            start()
        elif restart.upper() == "N":
            print("\nShuting down game.\n")
            sys.exit()
        else:
            print("Invalid comand, please try agian..")

#end games

def game_end_lose(msg):
    print(msg)
    restart()

def game_end_win():
    print("You won!")
    restart()

start()
