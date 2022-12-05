import string

PRIORITIES = {item: index + 1 for index, item in enumerate(string.ascii_letters)}


def get_common_character(string1, string2):
    for char in string1:
        if char in string2:
            return char


with open("input.txt") as fd:
    rucksacks = fd.read().split("\n")
    rucksacks_split = [[r[: (len(r) // 2)], r[(len(r) // 2) :]] for r in rucksacks]

    total_priorities = 0
    for left_comp, right_comp in rucksacks_split:
        common_item = get_common_character(left_comp, right_comp)
        total_priorities += PRIORITIES[common_item]
    print(total_priorities)
