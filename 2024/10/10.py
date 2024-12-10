coords = {x+1j*y: int(c) for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

def traverse(c, unique, some=0):
    if coords[c] == 9: 
        unique.add(c)
        return 1
    for d in [1, 1j, -1, -1j]:
        if coords.get(c+d) == coords[c] + 1:
            some += traverse(c+d, unique)
    return some

s1, p2 = 0, {c: set() for c in coords}
for c in coords:
    if coords[c] == 0:
        s1 += traverse(c, p2[c])

print(s1)
print(sum(map(len, p2.values())))
