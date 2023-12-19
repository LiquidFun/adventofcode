import re
import math
instructions, queries = open(0).read().split('\n\n')

rules = {}

def is_accepted(x, m, a, s, rule):
    if len(rule) == 1:
        if rule[0][0] in rules:
            return is_accepted(x, m, a, s, rules[rule[0][0]])
        return rule[0][0] == 'A'
    condition, trueval = rule[0]
    if eval(condition):
        return is_accepted(x, m, a, s, [[trueval]])
    return is_accepted(x, m, a, s, rule[1:])

def range_combinations(ranges, rule):
    if len(rule) == 1:
        if (curr := rule[0][0]) in rules:
            return range_combinations(ranges, rules[curr])
        return math.prod(map(len, ranges.values())) * (curr == 'A')
    (var, op, *digits), trueval = rule[0]
    num = int(''.join(digits)) + (op == '>')
    lower = range(ranges[var].start, num)
    upper = range(num, ranges[var].stop)

    rtrue = ranges | {var: lower if op == '<' else upper}
    rfalse = ranges | {var: upper if op == '<' else lower}
    return range_combinations(rtrue, [[trueval]]) \
         + range_combinations(rfalse, rule[1:])


for inst in instructions.splitlines():
    name, conditions = inst.strip("}").split("{")
    rules[name] = [rule.split(":") for rule in conditions.split(',')]

s = 0
for query in queries.splitlines():
    xmas = [int(a) for a in re.findall("(\d+)", query)]
    if is_accepted(*xmas, rules["in"]):
        s += sum(xmas)

print(s)
ranges = {key: range(1, 4001) for key in "xmas"}
print(range_combinations(ranges, rules['in']))
