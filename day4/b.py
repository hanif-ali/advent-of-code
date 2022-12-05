def ranges_overlap(range1, range2):
    total_range = abs((range1[1] - range1[0]) + (range2[1] - range2[0]))
    mutual_range = max(range1[1], range2[1]) - min(range1[0], range2[0])

    return total_range >= mutual_range


with open("input.txt") as fd:
    lines = fd.read().split("\n")

    pairs = [line.split(",") for line in lines]

    overlap_count = 0
    for left, right in pairs:
        left_range = [int(l) for l in left.split("-")]
        right_range = [int(l) for l in right.split("-")]

        if ranges_overlap(left_range, right_range):
            overlap_count += 1

    print(overlap_count)
