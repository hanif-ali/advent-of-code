"""
To accomodate the floor, I have used a custom CaveMap class instead of the defaultdict
This class keeps the map as well as the limits (which are generated using updatelimits)

The custom CaveMap behaves just like a defaultdict (returning AIR for any key not in the map) except that
it returns ROCK for any key that corresponds to the floor.
"""
from collections import defaultdict


class CaveMap:
    def __init__(self):
        self.map = defaultdict(lambda: ".")
        self.map_limits = (float("inf"), float("-inf"), float("inf"), float("-inf"))

    def __getitem__(self, key):
        if key[1] >= self.map_limits[3] + 2:
            return ROCK
        return self.map[key]

    def __setitem__(self, key, value):

        self.map[key] = value

    def update_limits(self):
        min_x = min(x for x, y in cavemap.map.keys())
        max_x = max(x for x, y in cavemap.map.keys())
        min_y = min(y for x, y in cavemap.map.keys())
        max_y = max(y for x, y in cavemap.map.keys())
        self.map_limits = (min_x, max_x, min_y, max_y)


with open("input.txt") as fd:
    structures = fd.read().split("\n")

ROCK = "#"
AIR = "."
SETTLED_SAND = "O"
FALLING_SAND = "+"

cavemap = CaveMap()


def draw_map(map, space_around=5):
    """
    Visualize the cave map. You can use space_around to add some space around the map.
    """
    (min_x, max_x, min_y, max_y) = map.map_limits

    min_x = min_x - space_around
    max_x = max_x + space_around
    min_y = min_y - space_around
    max_y = max_y + space_around

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(map[(x, y)], end="")
        print()


def build_structures(cavemap, structures):
    """
    Modify cavemap to add the rock structures as represented by `structure`.
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
            cavemap[point] = ROCK

            if last_point:
                if last_point[0] != point[0]:
                    start = min(last_point[0], point[0])
                    end = max(last_point[0], point[0])
                    for i in range(start, end):
                        cavemap[(i, point[1])] = ROCK
                elif last_point[1] != point[1]:
                    start = min(last_point[1], point[1])
                    end = max(last_point[1], point[1])
                    for i in range(start, end):
                        cavemap[(point[0], i)] = ROCK
                else:
                    raise "Should not be reachable. Points for lines should be different"
            last_point = point


def next_sand_position(cavemap, current_position):
    """
    From the current_position, determine the next step position of the sand
    Return the current step, if the sand settles
    Return VOID if the sand falls out of the canvas
    """
    one_step_down = (current_position[0], current_position[1] + 1)
    if cavemap[one_step_down] == AIR:
        return one_step_down

    diagonal_left = (current_position[0] - 1, current_position[1] + 1)
    if cavemap[diagonal_left] == AIR:
        return diagonal_left

    diagonal_right = (current_position[0] + 1, current_position[1] + 1)
    if cavemap[diagonal_right] == AIR:
        return diagonal_right

    return current_position


def drop_sand(cavemap, position):
    """
    Make one sand fall from the given position. Keep moving until the sand settles or falls our of canvas
    Return the position where the sand settles or VOID if the sand falls out of canvas
    """
    while (next_position := next_sand_position(cavemap, position)) != position:
        # cavemap[position] = FALLING_SAND
        # draw_map(cavemap)
        # cavemap[position] = AIR
        # print()
        position = next_position

    cavemap[position] = SETTLED_SAND
    return position


build_structures(cavemap, structures)
cavemap.update_limits()

sand_dropping_position = (500, 0)

while (
    drop_position := drop_sand(cavemap, sand_dropping_position)
) != sand_dropping_position:
    ...

draw_map(cavemap)
print("Total Settle units: ", sum(1 for x in cavemap.map.values() if x == SETTLED_SAND))
