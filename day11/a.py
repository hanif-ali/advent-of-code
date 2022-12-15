from typing import List


class Item:
    def __init__(self, worry_level: int):
        self.worry_level = worry_level

    def __repr__(self):
        return f"Item({self.worry_level})"


class Monkey:
    MONKEYS = []

    def __init__(
        self,
        items: List[Item],
        operation: str,
        test_divisor: str,
        true_target: int,
        false_target: int,
    ):
        self.items = items
        self.test_divisor = test_divisor
        self.operation = operation
        self.true_target = true_target
        self.false_target = false_target
        self.items_inspected = 0

    @classmethod
    def create(
        cls,
        items: List[Item],
        operation: str,
        test_divisor: int,
        true_target: int,
        false_target: int,
    ):
        monkey = Monkey(items, operation, test_divisor, true_target, false_target)
        cls.MONKEYS.append(monkey)

    def inspect(self):
        # Need it because self.items is mutated when calling inspect
        items_copy = self.items[:]
        for item in items_copy:
            self.inspect_item(item)

    def inspect_item(self, item: Item):
        item.worry_level = eval(self.operation.replace("old", str(item.worry_level)))
        item.worry_level = item.worry_level // 3

        if (item.worry_level % self.test_divisor) == 0:
            self.throw_to(item, self.true_target)
        else:
            self.throw_to(item, self.false_target)
        self.items_inspected += 1

    def throw_to(self, item: Item, target: int):
        Monkey.MONKEYS[target].items.append(item)
        self.items.remove(item)

    @classmethod
    def run_rounds(cls, num_rounds: int) -> None:
        for i in range(num_rounds):
            for monkey in cls.MONKEYS:
                monkey.inspect()

    def __repr__(self):
        return f"Monkey<{self.items}, inspected={self.items_inspected}>"


def parse_items_line(items_line: str) -> List[Item]:
    items_part = items_line.split(":")[1]
    items = items_part.split(",")
    items_as_int = [int(i.strip()) for i in items]
    return [Item(i) for i in items_as_int]


def parse_operation(operation_line: str) -> str:
    return operation_line.split("=")[1].strip()


def parse_test_divisor(divisor_line: str) -> int:
    return int(divisor_line.split("divisible by")[1].strip())


def parse_target_monkey_index(divisor_line: str) -> int:
    return int(divisor_line.split("throw to monkey")[1].strip())


with open("input.txt") as fd:
    monkeys_data = [chunk.split("\n") for chunk in fd.read().split("\n\n")]

for lines in monkeys_data:
    items = parse_items_line(lines[1])
    operation = parse_operation(lines[2])
    test_divisor = parse_test_divisor(lines[3])
    true_target_monkey_index = parse_target_monkey_index(lines[4])
    false_target_monkey_index = parse_target_monkey_index(lines[5])

    Monkey.create(
        items=items,
        operation=operation,
        test_divisor=test_divisor,
        true_target=true_target_monkey_index,
        false_target=false_target_monkey_index,
    )

Monkey.run_rounds(20)
inspections = [monkey.items_inspected for monkey in Monkey.MONKEYS]
top = max(inspections)
inspections.remove(top)
second_top = max(inspections)
print("Monkey Business: ", top * second_top)
