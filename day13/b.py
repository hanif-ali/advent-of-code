"""
In part (a) we wrote the algorithm to "compare" two packets.

Here we can simply expand our list of packets so that they are not longer in pairs. Then we can 
use the algorithm in part (a) to sort the packets using the native "sort" function. 
(We can also write our own sort function, but that is not the point of this exercise

We use cmp_to_key to use the existing comparator as a key for sorting
"""
from logging import getLogger
from typing import List, Tuple
from functools import cmp_to_key
import pprint

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


def sort_key(item1, item2):
    return check_pair_ordering((item1, item2))


packets = [i for sublist in pairs for i in sublist]
packets = [*packets, [[2]], [[6]]]  # Add divider packets
packets.sort(key=cmp_to_key(sort_key), reverse=True)

index_divider_1 = packets.index([[2]])
index_divider_2 = packets.index([[6]])
print(index_divider_1)
print(index_divider_2)
print("Decoder Key: ", (index_divider_1 + 1) * (index_divider_2 + 1))
