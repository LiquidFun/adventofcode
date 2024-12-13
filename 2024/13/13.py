import re
import z3

s = [0, 0]
for machine in open(0).read().split("\n\n"):
    (ax,ay), (bx,by), (px,py) = [map(int, x) for x in re.findall(r"(\d+).*?(\d+)", machine)]

    for i, add in enumerate([0, 10000000000000]):
        a, b = z3.Int('a'), z3.Int('b')

        solver = z3.Optimize()
        solver.add(px + add == a * ax + b * bx)
        solver.add(py + add == a * ay + b * by)
        solver.minimize(a * 3 + b)

        if solver.check() == z3.sat:
            model = solver.model()
            s[i] += model.eval(a).as_long() * 3 + model.eval(b).as_long()
print(*s, sep="\n")
