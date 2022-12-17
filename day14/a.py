"""
We represent the structure as a map of (x, y) -> char where char represent the type of the unit (AIR, ROCK, SETTLED_SAND, FALLING_SAND)

At any point, we can easily map out our structure using draw_map. This is also possible during the simulation to see how the sand is moving.
To see that in action, uncomment the lines in drop_sand.

"""
from collections import defaultdict

with open("input.txt") as fd:
    structures = fd.read().split("\n")

ROCK = "#"
AIR = "."
SETTLED_SAND = "O"
FALLING_SAND = "+"

CAVEMAP = defaultdict(lambda: ".")
VOID = (float("-inf"), float("inf"))


def draw_map(map, map_limits, space_around=5):
    """
    Visualize the cave map. You can use space_around to add some space around the map.
    """
    (min_x, max_x, min_y, max_y) = map_limits

    min_x = min_x - space_around
    max_x = max_x + space_around
    min_y = min_y - space_around
    max_y = max_y + space_around

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(map[(x, y)], end="")
        print()


def build_structures(CAVEMAP, structures):
    """
    Modify CAVEMAP to add the rock structures as represented by `structure`.
    Connect points in the structures by filling in the intermediate units
    """
    for structure in structures:
        points = structure.split(" -> ")
        points = [
            (int(point.split(",")[0]), int(point.split(",")[1])) for point in points
        ]

        last_point = None
        # Connect points
        for point in points:
            CAVEMAP[point] = ROCK

            if last_point:
                if last_point[0] != point[0]:
                    start = min(last_point[0], point[0])
                    end = max(last_point[0], point[0])
                    for i in range(start, end):
                        CAVEMAP[(i, point[1])] = ROCK
                elif last_point[1] != point[1]:
                    start = min(last_point[1], point[1])
                    end = max(last_point[1], point[1])
                    for i in range(start, end):
                        CAVEMAP[(point[0], i)] = ROCK
                else:
                    raise "Should not be reachable. Points for lines should be different"
            last_point = point


def position_is_void(position, map_limits):
    """
    Checks whether the positions falls out of the canvas (i.e. the sand would be lost from this position)
    """
    if position[0] < map_limits[0] or position[0] > map_limits[1]:
        return True
    if position[1] > map_limits[3]:
        return True
    return False


def next_sand_position(cavemap, current_position, map_limits):
    """
    From the current_position, determine the next step position of the sand
    Return the current step, if the sand settles
    Return VOID if the sand falls out of the canvas
    """
    one_step_down = (current_position[0], current_position[1] + 1)
    if position_is_void(one_step_down, map_limits):
        return VOID
    if cavemap[one_step_down] == AIR:
        return one_step_down

    diagonal_left = (current_position[0] - 1, current_position[1] + 1)
    if position_is_void(diagonal_left, map_limits):
        return VOID
    if cavemap[diagonal_left] == AIR:
        return diagonal_left

    diagonal_right = (current_position[0] + 1, current_position[1] + 1)
    if position_is_void(diagonal_right, map_limits):
        return VOID
    if cavemap[diagonal_right] == AIR:
        return diagonal_right

    return current_position


def drop_sand(cavemap, position, map_limits):
    """
    Make one sand fall from the given position. Keep moving until the sand settles or falls our of canvas
    Return the position where the sand settles or VOID if the sand falls out of canvas
    """
    while (
        next_position := next_sand_position(cavemap, position, map_limits)
    ) != position:
        if next_position == VOID:
            return VOID
        # cavemap[position] = FALLING_SAND
        # draw_map(cavemap, map_limits)
        # cavemap[position] = AIR
        # print()
        position = next_position

    cavemap[position] = SETTLED_SAND
    return position


build_structures(CAVEMAP, structures)
min_x = min(x for x, y in CAVEMAP.keys())
max_x = max(x for x, y in CAVEMAP.keys())
min_y = min(y for x, y in CAVEMAP.keys())
max_y = max(y for x, y in CAVEMAP.keys())
map_limits = (min_x, max_x, min_y, max_y)

sand_dropping_position = (500, 0)

while (
    settled_position := drop_sand(CAVEMAP, sand_dropping_position, map_limits)
) != VOID:
    ...

draw_map(CAVEMAP, map_limits)
print("Total Settle units: ", sum(1 for x in CAVEMAP.values() if x == SETTLED_SAND))
