"""
We use a modified version of Dijkstra's algorithm to find the shortest path
for each position in the 2d array

We consider each position in the heightmap as a node in a graph. Weights are the
differences between heights. 
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


def get_position(grid, character):
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == character:
                return (row_index, col_index)
    raise "Should not occur"


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


start_position = get_position(grid, "S")
target_position = get_position(grid, "E")
DISTANCES = find_shortest_path(grid, start_position, target_position)
print(DISTANCES.get(target_position))
