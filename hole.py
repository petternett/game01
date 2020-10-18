from random import randint


def generate_hole():
    x = randint(-10, 10)
    y = randint(-10, 10)
    return (x, y)


def main():
    cur_x = 1
    cur_y = 1

    
    while ((hole := generate_hole()) == (cur_x, cur_y)): pass

    print(f"x: {cur_x}, y: {cur_y}")
    print(f"hole: {hole}")


main()
