def solve(instructions, s=2, xy=0.):
    for d in instructions:
        s += abs(d.real+d.imag) + d.imag*xy.real - d.real*xy.imag
        xy += d
    print(int(s // 2))

split = [line.split() for line in open(0)]
solve(1j**"RDLU".index(d) * int(num) for d, num, _ in split)
solve(1j**int(c[7]) * int(c[2:7], 16) for *_, c in split)
