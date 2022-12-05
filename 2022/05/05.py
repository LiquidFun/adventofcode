import sys, re
towers, instructions = sys.stdin.read().rstrip().split("\n\n")
*towers, indices = towers.split("\n")
tower_count = int(indices.strip().split()[-1])

stacks1 = [[] for _ in range(tower_count)]

for line in towers[::-1]:
    for i in range(tower_count):
        c = line[i*4+1]
        if c != ' ':
            stacks1[i].append(c)

stacks2 = [l.copy() for l in stacks1]

for line in instructions.split("\n"):
    a, b, c = map(int, re.fullmatch(r"move (\d+) from (\d+) to (\d+)", line).groups())
    for _ in range(a):
        new = stacks1[b-1].pop()
        stacks1[c-1].append(new)

    stacks2[c-1].extend(stacks2[b-1][-a:])
    for _ in range(a):
        stacks2[b-1].pop()

print(''.join(s[-1] for s in stacks1))
print(''.join(s[-1] for s in stacks2))
