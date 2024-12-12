coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

dir_corners = [.5+.5j, .5-.5j, -.5+.5j, -.5-.5j]
def adjacent(coord, dirs=[1, 1j, -1, -1j]):
    return [coord + d for d in dirs]

regions, visited = [], set()

def fill_region(c, region):
    visited.add(c)
    region.append(c)
    for adj in adjacent(c):
        if coords.get(adj) == coords[c] and adj not in visited:
            fill_region(adj, region)
    return region

for c, char in coords.items():
    if c not in visited:
        regions.append((char, fill_region(c, [])))

s1 = s2 = 0
for char, region in regions:
    perimeter = 0
    for r in region:
        for adj in adjacent(r):
            if coords.get(adj) != char and adj not in region:
                perimeter += 1
    s1 += perimeter * len(region)

    corners = set()
    for r in region:
        for corner in adjacent(r, dir_corners):
            k = [adj for adj in adjacent(corner, dir_corners) if adj in region]
            if len(k) in [1, 3]:
                corners.add(corner)
            elif abs(k[0] - k[1]) != 1:
                corners |= {corner, corner+0.1}

    s2 += len(corners) * len(region)

print(s1, s2, sep="\n")
