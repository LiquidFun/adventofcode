
import z3

lines = open(0).read().splitlines()

sx, sy, sz = z3.Real('x'), z3.Real('y'), z3.Real('z')
sdx, sdy, sdz = z3.Real('dx'), z3.Real('dy'), z3.Real('dz')
solver = z3.Solver()

coords = []
for i, line in enumerate(lines):
    x, y, z, dx, dy, dz = map(int, line.replace("@", ",").split(","))
    coords.append((x, y, z, dx, dy, dz))
    if i < 3:
        t = z3.Real(f't{i}')
        solver.add(sx + sdx * t == x + dx * t)
        solver.add(sy + sdy * t == y + dy * t)
        solver.add(sz + sdz * t == z + dz * t)


s1 = 0
for i, (x1, y1, z1, dx1, dy1, dz1) in enumerate(coords):
    for x2, y2, z2, dx2, dy2, dz2 in coords[i+1:]:
        slope1 = dy1 / dx1
        slope2 = dy2 / dx2
        b1 = y1 - slope1 * x1
        b2 = y2 - slope2 * x2
        if slope1 != slope2:
            ix = (b2 - b1) / (slope1 - slope2)
            iy = slope1 * ix + b1

            if 2e14 <= ix <= 4e14 and 2e14 <= iy <= 4e14:
                if (x1 - ix) * dx1 < 0 and (x2 - ix) * dx2 < 0:
                    if (y1 - iy) * dy1 < 0 and (y2 - iy) * dy2 < 0:
                        s1 += 1

print(s1)
assert solver.check() == z3.sat
model = solver.model()
get = lambda var: model.eval(var).as_long()
print(get(sx) + get(sy) + get(sz))
