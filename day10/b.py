with open("input.txt") as fd:
    instructions = fd.read().split("\n")

signal_strengths = []
next_key_cycle = 20
current_cycle = 1
X = 1


def draw_pixel():
    global current_cycle, X
    if abs((current_cycle - 1) % 40 - X) <= 1:
        print("#", end="")
    else:
        print(".", end="")

    if current_cycle % 40 == 0:
        print()


def perform_cycles(number_of_cycles: int):
    global current_cycle, signal_strengths, X, next_key_cycle
    for i in range(number_of_cycles):
        draw_pixel()
        if current_cycle == next_key_cycle:
            signal_strengths.append(current_cycle * X)
            next_key_cycle += 40
        current_cycle += 1


for instruction in instructions:
    parts = instruction.split()

    if parts[0] == "noop":
        perform_cycles(1)
    elif parts[0] == "addx":
        perform_cycles(2)
        X += int(parts[1])
    else:
        raise "Not reachable"
