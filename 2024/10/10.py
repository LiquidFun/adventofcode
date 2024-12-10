coords = {x+1j*y: int(c) for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

def traverse(c, unique, some=0):
    if coords[c] == 9: 
        unique.add(c)
        return 1
    for d in [1, 1j, -1, -1j]:
        if coords.get(c+d) == coords[c] + 1:
            some += traverse(c+d, unique)
    return some

p1, s2 = {c: set() for c in coords}, 0
for c in coords:
    if coords[c] == 0:
        s2 += traverse(c, p1[c])

print(sum(map(len, p1.values())))
print(s2)
