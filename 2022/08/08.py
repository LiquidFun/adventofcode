import sys
s = [list(a) for a in sys.stdin.read().strip().split("\n")]

# === Part 1 ===
visible = set()
indices = list(range(len(s)))
for i in indices:
    for order in (indices, list(reversed(indices))):
        m = '/'
        for x in order:
            if m < s[i][x]:
                visible.add((i, x))
            m = max(s[i][x], m)
        m = '/'
        for y in order:
            if m < s[y][i]:
                visible.add((y, i))
            m = max(s[y][i], m)
print(len(visible))

# === Part 2 ===
best = 0
is_valid = lambda y, x: 0 <= y < len(s) and 0 <= x < len(s[0])
for Y in range(len(s)):
    for X in range(len(s[0])):
        scenic = 1
        for ya, xa in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dist, y, x = 0, Y+ya, X+xa
            while is_valid(y, x):
                dist += 1
                if s[y][x] >= s[Y][X]:
                    break
                y, x = y+ya, x+xa
            scenic *= dist
        best = max(best, scenic)
print(best)
