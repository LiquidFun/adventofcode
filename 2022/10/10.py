import sys
X, s = 1, 0
crt = [[] for _ in range(6)]
for cycle, line in enumerate(sys.stdin.read().replace(" ", "\n").split()):
    crt[cycle // 40].append('#' if X - 1 <= cycle % 40 <= X + 1 else ' ')
    if (cycle+1) % 40 == 20:
        s += X * (cycle+1)
    if line not in ["addx", "noop"]:
        X += int(line)
print(s)
print(*[''.join(line) for line in crt], sep='\n')
