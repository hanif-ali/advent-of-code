def find_first_unique_four(string):
    """
    Return start index of first unique four characters
    Return -1 if not found
    """
    if len(string) < 4:
        return -1

    start = 0
    end = 4
    found = False
    while end < len(data):
        # If all characters are unique
        if len(set(data[start:end])) == 4:
            found = True
            break
        start += 1
        end += 1

    if not found:
        return -1
    return start


with open("input.txt") as fd:
    data = fd.read()
    first_unique_four_index = find_first_unique_four(data)
    if first_unique_four_index == -1:
        print("Not found")
    else:
        print(first_unique_four_index + 4)
