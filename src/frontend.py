#Allisons responsibility
#render grid and display game pieces
#Score info and user input?

GRID_SIZE = 6
PLAYER = "P"
EMPTY = "."


def new_grid():
    grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    grid[0][0] = PLAYER
    return grid


def render(grid, score=0):
    print()
    for row in grid:
        print(" ".join(row))
    print(f"Score: {score}")


def run():
    grid = new_grid()
    score = 0

    while True:
        render(grid, score)
        move = input("Move (w/a/s/d, q to quit): ").strip().lower()

        if move == "q":
            print("Quitting game.")
            break
        elif move in ("w", "a", "s", "d"):
            print(f"Move '{move}' received.")
        else:
            print("Invalid input.")
