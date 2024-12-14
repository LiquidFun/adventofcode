import re

X, Y = 101, 103
nums = [list(map(int, re.findall(r"-?\d+", line))) for line in open(0)]

for i in range(X * Y):
    quadrant = [0, 0, 0, 0]
    picture = [" "] * (X * Y)
    for x, y, vx, vy in nums:
        nx = (x + vx * i) % X
        ny = (y + vy * i) % Y
        picture[ny * X + nx] = "#"
        if nx != X//2 and ny != Y//2:
            quadrant[(nx > X//2) + (ny > Y//2) * 2] += 1

    if i == 100:
        print(quadrant[0] * quadrant[1] * quadrant[2] * quadrant[3])

    if ("#" * 20) in ''.join(picture):
        print(i)
        break
