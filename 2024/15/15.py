def solve(field, gps=0):
    coords = {x+1j*y: c for y, r in enumerate(field.split("\n")) for x, c in enumerate(r)}

    s = [c for c, char in coords.items() if char == "@"][0]
    coords[s] = "."

    def collect(c):
        if coords[c+d] not in "]O[":
            return {}
        dn = d + ("]O[".index(coords[c+d]) - 1 if d.imag else 0) 
        return {c+d: coords[c+d], c+dn: coords[c+dn]} \
               | collect(c+d) \
               | collect(c+dn)

    for m in moves.replace("\n", ""):
        d = {'>': 1, 'v': 1j, '<': -1, '^': -1j}[m]
        
        if coords[s + d] != '#':
            boxes = collect(s)
            for x, char in boxes.items():
                if coords[x+d] == '#':
                    break
            else:
                for x, char in boxes.items():
                    coords[x] = '.'
                for x, char in boxes.items():
                    coords[x+d] = char
                s = s+d
        
    print(int(sum(x.imag * 100 + x.real for x, c in coords.items() if c in '[O')))


field, moves = open(0).read().split("\n\n")

solve(field)
for r1, r2 in [("#", "##"), ("O", "[]"), (".", ".."), ("@", "@.")]:
    field = field.replace(r1, r2)
solve(field)
