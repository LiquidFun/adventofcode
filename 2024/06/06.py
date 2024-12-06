coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r) if c != '\n'}

for pos, c in coords.items():
    if c == "^":
        start = pos

def solve(obstruction, pos=start, d=-1j):
    seen = set()
    while pos in coords:
        seen.add((pos, d))
        while coords.get(pos + d, "#") != '#' and pos + d != obstruction:
            pos += d
            seen.add((pos, d))
        if pos + d not in coords:
            return {p for p, _ in seen}
        d *= 1j
        if (pos, d) in seen:
            return True

seen = solve(-1)
print(len(seen), sum(solve(coord) is True for coord in seen))
