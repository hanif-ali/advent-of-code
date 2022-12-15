"""
For this part, ideally we should change the algorithm in a way that after the algorithm is run,
we can query the path from any position to any other position.

However, for the input size of the contest, simply running the algorithm for each starting position
and then finding the min of distances to the end position is fast enough. So this code does that.
"""
from collections import defaultdict

with open("input.txt") as fd:
    # grid is 2d list of the heights
    grid = [list(line) for line in fd.read().split("\n")]


def get_elevation(grid, position):
    height_char = grid[position[0]][position[1]]
    if height_char == "S":
        return 0
    elif height_char == "E":
        return 25
    return "abcdefghijklmnopqrstuvwxyz".index(height_char)


def get_positions(grid, character):
    positions = []
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == character:
                positions.append((row_index, col_index))
    return positions


def get_weights(grid, start_position):
    """
    Return the weights for each direction
    """
    weights = [float("inf")] * 4  # up, right, down, left
    current_elevation = get_elevation(grid, start_position)

    if start_position[0] != 0:
        weights[0] = (
            get_elevation(grid, (start_position[0] - 1, start_position[1]))
            - current_elevation
        )
    if start_position[1] != len(grid[0]) - 1:
        weights[1] = (
            get_elevation(grid, (start_position[0], start_position[1] + 1))
            - current_elevation
        )
    if start_position[0] != len(grid) - 1:
        weights[2] = (
            get_elevation(grid, (start_position[0] + 1, start_position[1]))
            - current_elevation
        )
    if start_position[1] != 0:
        weights[3] = (
            get_elevation(grid, (start_position[0], start_position[1] - 1))
            - current_elevation
        )
    return tuple(weights)


def find_shortest_path(grid, start_position, target_position):
    DISTANCES = defaultdict(lambda: float("inf"))
    DISTANCES[start_position] = 0
    VISITED = {}

    to_check = [start_position]
    while to_check:
        position = to_check.pop(0)

        if position == target_position or position in VISITED:
            continue

        VISITED[position] = True

        weights = get_weights(grid, position)
        up_position = (position[0] - 1, position[1])
        right_position = (position[0], position[1] + 1)
        down_position = (position[0] + 1, position[1])
        left_position = (position[0], position[1] - 1)

        if weights[0] <= 1:
            if DISTANCES[position] + 1 < DISTANCES[up_position]:
                DISTANCES[up_position] = DISTANCES[position] + 1
                to_check.append(up_position)
        if weights[1] <= 1:
            if DISTANCES[position] + 1 < DISTANCES[right_position]:
                DISTANCES[right_position] = DISTANCES[position] + 1
                to_check.append(right_position)
        if weights[2] <= 1:
            if DISTANCES[position] + 1 < DISTANCES[down_position]:
                DISTANCES[down_position] = DISTANCES[position] + 1
                to_check.append(down_position)
        if weights[3] <= 1:
            if DISTANCES[position] + 1 < DISTANCES[left_position]:
                DISTANCES[left_position] = DISTANCES[position] + 1
                to_check.append(left_position)

    return DISTANCES


start_positions = [get_positions(grid, "S")[0], *get_positions(grid, "a")]
target_position = get_positions(grid, "E")[0]

distances_from_different_starts = []
for start_position in start_positions:
    DISTANCES = find_shortest_path(grid, start_position, target_position)
    shortest_distance = DISTANCES.get(target_position)
    if shortest_distance:
        distances_from_different_starts.append(shortest_distance)

print(min(distances_from_different_starts))
