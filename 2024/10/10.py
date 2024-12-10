coords = {x+1j*y: int(h) for y, r in enumerate(open(0)) for x, h in enumerate(r.strip())}

def hike(c, peaks, paths=0):
    if coords[c] == 9: 
        peaks.add(c)
        return 1
    for d in [1, 1j, -1, -1j]:
        if coords.get(c+d) == coords[c] + 1:
            paths += hike(c+d, peaks)
    return paths

p1, s2 = {c: set() for c in coords}, 0
for c in coords:
    if coords[c] == 0:
        s2 += hike(c, p1[c])

print(sum(map(len, p1.values())))
print(s2)
