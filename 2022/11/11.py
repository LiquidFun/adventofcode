import sys, math, operator

monkeys = []

class Monkey:
    modulo = 1
    def __init__(self, monkey: str):
        _, items, op, test, if_t, if_f = monkey.split("\n")
        self.items = [int(a) for a in items.split(":")[1].split(',')]
        ops = {"*": operator.mul, "+": operator.add}
        *_, op, arg = op.split(":")[1].split()
        self.op = lambda x: ops[op](x, x if arg == "old" else int(arg))
        self.divisible_by = int(test.split()[-1])
        Monkey.modulo *= self.divisible_by
        self.if_t = int(if_t.split()[-1])
        self.if_f = int(if_f.split()[-1])
        self.passes = 0

    def round(self, div_by_3: bool):
        for item in self.items:
            new_worry = self.op(item) // (3 if div_by_3 else 1) % Monkey.modulo
            self.passes += 1
            new_index = self.if_t if new_worry % self.divisible_by == 0 else self.if_f
            monkeys[new_index].items.append(new_worry)
        self.items.clear()


monkeys2 = []
for i, monkey in enumerate(sys.stdin.read().strip().split("\n\n")):
    monkeys.append(Monkey(monkey))
    monkeys2.append(Monkey(monkey))

for i in range(20):
    for monkey in monkeys:
        monkey.round(True)
print(math.prod(sorted([a.passes for a in monkeys])[-2:]))

monkeys = monkeys2
for i in range(10000):
    for monkey in monkeys:
        monkey.round(False)
print(math.prod(sorted([a.passes for a in monkeys])[-2:]))
