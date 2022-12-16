"""
We use a recursive function to compare a pair of items. Item can be an arbitarily nested list
or a single integer.
"""

from logging import getLogger
from typing import List, Tuple

logger = getLogger(__name__)
logger.disabled = True

ORDERED = 1  # Correct ordering
AMBIGUOUS = 0  # Ordering is same, continue checking the input
UNORDERED = -1  # Wrong Ordering

with open("input.txt") as fd:
    pairs = fd.read().split("\n\n")
    pairs = [(eval(p.split("\n")[0]), eval(p.split("\n")[1])) for p in pairs]

# Pairs is in the format [(list1a, list1b), (list1a, list2b), ...] where each listxx is an
# arbitarily nested list


def check_pair_ordering(pair: Tuple[List | int, List | int], depth=0) -> int:
    left = pair[0]
    right = pair[1]

    logger.debug(f"{' ' * depth}- {left} vs {right}")
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return ORDERED
        elif left == right:
            return AMBIGUOUS
        else:
            return UNORDERED
    elif isinstance(left, list) and isinstance(right, list):
        for index in range(max(len(left), len(right))):
            if index >= len(left):
                return ORDERED
            if index >= len(right):
                return UNORDERED

            result = check_pair_ordering((left[index], right[index]), depth + 4)
            if result != AMBIGUOUS:
                return result
        else:
            return AMBIGUOUS
    elif isinstance(left, list) and isinstance(right, int):
        return check_pair_ordering((left, [right]), depth + 4)
    elif isinstance(left, int) and isinstance(right, list):
        return check_pair_ordering(([left], right), depth + 4)
    else:
        raise "Should not happen"


orderings = [check_pair_ordering(i) for i in pairs]
index_sum = sum([i + 1 for i, j in enumerate(orderings) if j == ORDERED])
print("Index sum: ", index_sum)
