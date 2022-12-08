with open("input.txt") as fd:
    lines = fd.read().split("\n")


RIGHT = "RIGHT"
LEFT = "LEFT"
TOP = "TOP"
BOTTOM = "BOTTOM"


def check_scene(trees, row, column, target, direction):
    crow = row
    ccol = column

    while 0 <= crow < len(trees) and 0 <= ccol < len(trees[0]):
        current_tree_height = trees[crow][ccol]
        yield trees[crow][ccol]

        if current_tree_height >= target:
            break

        if direction == RIGHT:
            ccol += 1
        elif direction == LEFT:
            ccol -= 1
        elif direction == TOP:
            crow -= 1
        elif direction == BOTTOM:
            crow += 1


def get_scenic_score(trees, row, column):
    # We can use DP to improve the speed here
    # by building a table insetad of going through the whole row and column
    # for every entry

    tree_height = trees[row][column]

    scene_from_top = list(check_scene(trees, row - 1, column, tree_height, TOP))
    scene_from_bottom = list(check_scene(trees, row + 1, column, tree_height, BOTTOM))
    scene_from_left = list(check_scene(trees, row, column - 1, tree_height, LEFT))
    scene_from_right = list(check_scene(trees, row, column + 1, tree_height, RIGHT))

    return (
        len(scene_from_top)
        * len(scene_from_bottom)
        * len(scene_from_left)
        * len(scene_from_right)
    )


# Represent tree grid using a 2d array
trees = [list(map(int, list(line))) for line in lines]

scores = []

# Only iterate over the trees in the middle (not the edges)
for row_index in range(1, len(trees) - 1):
    for column_index in range(1, len(trees[0]) - 1):
        tree_height = trees[row_index][column_index]
        # Get the max heights around the tree
        scenic_score = get_scenic_score(trees, row_index, column_index)
        scores.append(scenic_score)
print(max(scores))
