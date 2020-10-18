import sys
import os
from random import randint


# Global variables
game_is_running = None
glob_msg = None
player_x = player_y = None
map_width = map_height = None
tile_map = None
hole = None


# Helper functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_msg(new_msg):
    global glob_msg
    glob_msg = new_msg

def print_message():
    print(glob_msg)
    print("\n")

def generate_hole():
    holeX = randint(0, width)
    holeY = randint(0, height)
    return (holeX, holeY)


# Is called at the start of the game
def start():
    global player_x, player_y
    global map_width, map_height
    global game_is_running
    global tile_map
    global hole

    map_width = 10
    map_height = 10
    # player_x = int(map_width / 2)
    # player_y = int(map_height / 2)
    player_x = player_y = 0
    game_is_running = True
    tile_map = []

    
    # Generate hole
    # while ((hole := generate_hole()) == (x, y)): pass
    hole = (player_x+1, player_y+1)

    # Populate tilemap
    tile_map = [["." for i in range(map_width)] for j in range(map_height)]
    tile_map[hole[1]][hole[0]] = "u"
    tile_map[player_x][player_y] = "x"

    set_msg("Welcome to the game. You need to enter a hole to win. Type 'quit' to exit.")

    update()


# Is called every "frame"
# (every time user makes a move)
def update():
    global player_x, player_y

    cam_hw = 5

    while (game_is_running):
        clear_screen()
        print_message()

        # Calculate map
        result = [["" for i in range(cam_hw)] for j in range(cam_hw)]

        i = player_y-1
        for y in range(0, cam_hw):
            if (i >= 0 and i < map_height):
                j = player_x-1
                for x in range(0, cam_hw):
                    if (j >= 0 and j < map_width):
                        # inside map - x axis
                        result[y][x] += tile_map[i][j]
                    elif (j == map_width or j == -1):
                        # outside map - x axis
                        result[y][x] += "|"

                    j += 1

            elif (i == map_height or i == -1):
                for x in range(0, cam_hw):
                    result[y][x] = "_"
            i += 1

        # Draw map
        for i in range(0, cam_hw):
            for j in range(0, cam_hw):
                print(result[i][j], end=" ")
            print()
        print("\n")


        cur_x = player_x
        cur_y = player_y

        move = input("Make a move (up/down/left/right): ")
        if move.lower() == "up":
            player_y -= 1
            tile_map[cur_y][cur_x] = "."
            tile_map[cur_y-1][cur_x] = "x"
        elif move.lower() == "down":
            player_y += 1
            tile_map[cur_y][cur_x] = "."
            tile_map[cur_y+1][cur_x] = "x"
        elif move.lower() == "left":
            player_x -= 1
            tile_map[cur_y][cur_x] = "."
            tile_map[cur_y][cur_x-1] = "x"
        elif move.lower() == "right":
            player_x += 1
            tile_map[cur_y][cur_x] = "."
            tile_map[cur_y][cur_x+1] = "x"
        elif move.lower() == "quit":
            sys.exit()
        else:
            set_msg("Invalid move, try again.")
            continue

        # Check if edge
        if (player_x > map_width or player_x < 0 or player_y > map_height or player_y < 0):
            game_over("Oh no, you fell over the edge..")
            sys.exit()

        # Check if hole
        if (player_x == hole[0] and player_y == hole[1]):
            game_over("You fell down a hole..")


        set_msg(f"You moved {move.lower()}, new position is {player_x}x, {player_y}y.")



def game_over(msg):
    print(msg)
    sys.exit()



start()
