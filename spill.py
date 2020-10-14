import sys
import os

holes = {
    "hole1" : {
        "x" : -3,
        "y" : 4
    },
    "hole2" : {
        "x" : 5,
        "y" : -2
    },
    "hole3" : {
        "x" : 7,
        "y" : -6
    }
}

rocks = {
    "rock1" : {
        "x" : 3,
        "y" : 4
    },
    "rock2" : {
        "x" : 2,
        "y" : -2
    },
    "rock3" : {
        "x" : -4,
        "y" : -6
    }
}

trees = {
    "tree1" : {
        "x" : -8,
        "y" : -3
    },
    "tree2" : {
        "x" : 4,
        "y" : -2
    },
    "tree3" : {
        "x" : 1,
        "y" : 3
    }
}

# Global variables
glob_msg = None
x = y = None


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_msg(new_msg):
    global glob_msg
    glob_msg = new_msg

def print_message():
    print(glob_msg)
    print("\n\n")


def start():
    x = y = 0
    set_msg("Welcome to the game.")

    update()


def update():
    x = y = 0

    while True:
        clear_screen()
        print_message()

        curX = x
        curY = y

        move = input("Make a move (up/down/left/right): ")
        if move.lower() == "up":
            y += 1
        elif move.lower() == "down":
            y -= 1
        elif move.lower() == "left":
            x -= 1
        elif move.lower() == "right":
            x += 1
        elif move.lower() == "quit":
            sys.exit()
        else:
            print("Invalid move, try again.")
            continue

        # Check if edge
        if (x >= 11 or x <= -11 or y >= 11 or y <= -11):
            game_over("Oh no, you fell over the edge..")
            sys.exit()

        # Check if hole
        for hole in holes.keys():
            checkX = holes[hole]["x"]
            checkY = holes[hole]["y"]

            if (x == checkX and y == checkY):
                game_over("Oh no, you fell down a hole..")


        # Check if tree
        def checkTree(x, y, trees):
            for tree in trees.keys():
                checkX = trees[tree]["x"]
                checkY = trees[tree]["y"]

                if (x == checkX and y == checkY):
                    x = curX
                    y = curY
                    set_msg("Oh no, you ran into a tree! Try another direction.")
                    return

        checkTree(x, y, trees)





        set_msg(f"You moved {move.lower()}, new position is {x}x, {y}y.")



def game_over(msg):
    print(msg)
    sys.exit()



start()
