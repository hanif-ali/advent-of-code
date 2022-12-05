import string

PRIORITIES = {item: index + 1 for index, item in enumerate(string.ascii_letters)}


def get_common_character(string1, string2, string3):
    for char in string1:
        if char in string2:
            if char in string3:
                return char


with open("input.txt") as fd:
    rucksacks = fd.read().split("\n")
    groups_of_three = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]

    total = 0
    for group in groups_of_three:
        common = get_common_character(group[0], group[1], group[2])
        total += PRIORITIES[common]
    print(total)
