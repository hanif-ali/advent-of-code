class Stack:
    def __init__(self):
        self.items = []

    # Push now supprts multiple items
    def push(self, *items):
        self.items.extend(items)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


def get_stacks_and_steps():
    with open("input.txt") as fd:
        (config, steps) = fd.read().split("\n\n")

        config = config.split("\n")
        steps = steps.split("\n")

        number_of_stacks = int(config[-1].split("   ")[-1].strip())

        stacks = [Stack() for _ in range(number_of_stacks)]

        for line in config[-2::-1]:
            for i in range(number_of_stacks):
                stack_position = 1 + i * 4
                letter = line[stack_position]
                if letter != " ":
                    stacks[i].push(letter)
        return [stacks, steps]


def apply_steps(stacks, steps):
    for step in steps:
        [count, source_index, destination_index] = (
            int(step.split(" ")[1]),
            int(step.split(" ")[3]) - 1,
            int(step.split(" ")[5]) - 1,
        )

        # Modify to push the number of items
        items_to_push = [stacks[source_index].pop() for _ in range(count)]
        # Reverse to maintin order
        items_to_push.reverse()

        stacks[destination_index].push(*items_to_push)


(stacks, steps) = get_stacks_and_steps()
apply_steps(stacks, steps)

answer = "".join([s.pop() for s in stacks])
print(answer)
