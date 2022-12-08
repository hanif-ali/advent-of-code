# first unique n
def first_first_unique_n(string: str, n: int) -> int:
    """
    Return start index of first unique `n` characters
    Return -1 if not found
    """
    if len(string) < n:
        return -1

    start = 0
    end = n
    found = False
    while end < len(data):
        # If all characters are unique
        if len(set(data[start:end])) == n:
            found = True
            break
        start += 1
        end += 1

    if not found:
        return -1
    return start


with open("input.txt") as fd:
    data = fd.read()
    first_unique_fourteen = first_first_unique_n(data, 14)
    if first_unique_fourteen == -1:
        print("Not found")
    else:
        print(first_unique_fourteen + 14)
