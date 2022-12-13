with open("input.txt") as fd:
    instructions = fd.read().split("\n")

signal_strengths = []
next_key_cycle = 20
current_cycle = 1
X = 1


def perform_cycles(number_of_cycles: int):
    global current_cycle, signal_strengths, X, next_key_cycle
    for i in range(number_of_cycles):
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

print(sum(signal_strengths))
