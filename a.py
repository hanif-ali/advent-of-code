with open("input.txt") as fp:
    data = fp.read()
    data_elf = data.split("\n\n")
    calories_elf = [list(map(int, d.split("\n"))) for d in data_elf]
    sums = [sum(c) for c in calories_elf]

    total = 0
    total += max(sums)
    sums.remove(max(sums))
    total += max(sums)
    sums.remove(max(sums))
    total += max(sums)
    print(total)
