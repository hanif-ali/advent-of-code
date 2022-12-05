def ranges_overlap(range1, range2):
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        print("Range 1 within range 2")
        return True
    if range2[0] >= range1[0] and range2[1] <= range1[1]:
        print("Range 2 within range 1")
        return True
    return False


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
