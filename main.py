matrix = [[]]
matrix_test = [["I", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "O"]]

compass = {"north": "south", "south": "north", "east": "west", "west": "east"}


def file_to_matrix(filename, total_lines=7, total_columns=8):
    m = [[0 for _ in range(total_columns)] for _ in range(total_lines)]
    line, column = 0, 0

    with open(filename) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            elif c == "\n":
                line += 1
                column = 0
            elif c != ' ':
                m[line][column] = c
                column += 1
    return m


def print_matrix():
    for line in matrix:
        for column in line:
            print(column, end="\t")
        print()
    print()


def initial_move():
    walk([1, 2])


def walk(new_pos):
    old_pos = get_runner_position()
    matrix[old_pos[0]][old_pos[1]], matrix[new_pos[0]][new_pos[1]] = 0, matrix[old_pos[0]][old_pos[1]]


def get_runner_position(runner="I"):
    runner_position = [-1, -1]
    for line, lineVal in enumerate(matrix):
        for column, columnVal in enumerate(lineVal):
            if columnVal == runner:
                runner_position = [line, column]
    return runner_position


def run(direction):
    print_matrix()

    runner_position = get_runner_position()
    walls = get_options(runner_position, walls=1)
    paths = get_options(runner_position, walls=0)
    # paths.pop(compass[direction], None)

    print("Going To -", direction)
    print("Coming From -", compass[direction])

    print("Walls -", walls)
    print("Paths -", paths)

    if len(walls) == 3:
        run(compass[direction])
    if len(paths) == 1:
        walk(list(dict.values(paths))[0])
        run(direction)
    # if len(paths) == 3:
    #     run(compass[going_to], going_to)
    # elif (4 - len(paths)) == 2:
    #     walk(paths[going_to])
    #     run(compass[going_to], going_to)


def get_options(position, walls):
    north = {"north": [position[0] - 1, position[1]]} if matrix[position[0] - 1][position[1]] == ("1" if walls == 1 else "0") else {}
    south = {"south": [position[0] + 1, position[1]]} if matrix[position[0] + 1][position[1]] == ("1" if walls == 1 else "0") else {}
    east = {"east": [position[0], position[1] + 1]} if matrix[position[0]][position[1] + 1] == ("1" if walls == 1 else "0") else {}
    west = {"west": [position[0], position[1] - 1]} if matrix[position[0]][position[1] - 1] == ("1" if walls == 1 else "0") else {}
    options = {**north, **south, **east, **west}
    return options


def main():
    global matrix
    matrix = file_to_matrix("maze.txt")

    initial_move()

    run("east")

main()
