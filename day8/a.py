with open("input.txt") as fd:
    lines = fd.read().split("\n")


def get_max_heights_around(trees, row, column):
    # We can use DP to improve the speed here
    # by building a table insetad of going through the whole row and column
    # for every entry

    total_rows = len(trees)
    total_cols = len(trees[0])

    max_from_top = max([trees[r][column] for r in range(row)])
    max_from_bottom = max([trees[r][column] for r in range(row + 1, total_rows)])
    max_from_left = max([trees[row][c] for c in range(column)])
    max_from_right = max([trees[row][c] for c in range(column + 1, total_cols)])

    return (max_from_top, max_from_right, max_from_bottom, max_from_left)


# Represent tree grid using a 2d array
trees = [list(map(int, list(line))) for line in lines]

hidden_trees = []
# Only iterate over the trees in the middle (not the edges)
for row_index in range(1, len(trees) - 1):
    for column_index in range(1, len(trees[0]) - 1):
        tree_height = trees[row_index][column_index]

        # Get the max heights around the tree
        heights_around = get_max_heights_around(trees, row_index, column_index)

        if min(heights_around) >= tree_height:
            print(f"Tree at ({row_index}, {column_index}) is hidden")
            hidden_trees.append((row_index, column_index))
        else:
            print(f"Tree at ({row_index}, {column_index}) is visible")

print("Total Hidden Trees: ", len(hidden_trees))
print("Total Visible Trees: ", len(trees) * len(trees[0]) - len(hidden_trees))
