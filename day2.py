def calculate(moves):
    horizontal_position, aim, depth = 0, 0, 0
    for move in moves:
        if move[0] == "down":
            aim += move[1]
        elif move[0] == "up":
            aim -= move[1]
        elif move[0] == "forward":
            horizontal_position += move[1]
            depth += aim * move[1]
        else:
            print("Wrong command")
    return horizontal_position * depth


with open("day2_input") as inp:
    moves = inp.readlines()

moves = [move.rstrip() for move in moves]
moves = [move.split() for move in moves]
moves = [(move[0], int(move[1])) for move in moves]
forwards = [move for move in moves if move[0] == "forward"]
downs = [move for move in moves if move[0] == "down"]
ups = [move for move in moves if move[0] == "up"]
print("answer", calculate(moves))
