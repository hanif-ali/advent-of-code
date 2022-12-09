# Approach
# The points are modelled as normal cartesian coordiantes
#   - We start at 0,0
#   - The y coordinate increases upwards and  x coordinate increases to the right

with open("input.txt") as fd:
    commands = fd.read().split("\n")


def adjust_tail_position(head_position, tail_position):
    """
    Adjusts the tail position given that there has been only one step since
    the last adjusted position
    """
    # If touching, don't do anything
    if (
        abs(head_position[0] - tail_position[0]) <= 1
        and abs(head_position[1] - tail_position[1]) <= 1
    ):
        return

    # Same row different columns
    if head_position[0] == tail_position[0]:
        tail_position[1] += 1 if head_position[1] > tail_position[1] else -1

    # Same column different rows
    elif head_position[1] == tail_position[1]:
        tail_position[0] += 1 if head_position[0] > tail_position[0] else -1

    # Both row and columns are different
    else:
        tail_position[0] += 1 if head_position[0] > tail_position[0] else -1
        tail_position[1] += 1 if head_position[1] > tail_position[1] else -1


positions_visited = {}

# index 0 is the H know, index 9 is the tail
knots = [[0, 0] for i in range(10)]
for command in commands:
    (direction, steps) = command.split(" ")
    steps = int(steps)

    for _ in range(steps):
        if direction == "U":
            knots[0][0] += 1
        elif direction == "D":
            knots[0][0] -= 1
        elif direction == "R":
            knots[0][1] += 1
        elif direction == "L":
            knots[0][1] -= 1

        for i in range(9):
            adjust_tail_position(knots[i], knots[i + 1])
        positions_visited[(knots[-1][0], knots[-1][1])] = True

print(len(positions_visited.keys()), "positions visited")
