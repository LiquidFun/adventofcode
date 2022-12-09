import sys
visited_segment2 = set()
visited_segment10 = set()
rope = [[0, 0] for _ in range(10)]
lookup = {"L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1)}
for dir, steps in [line.split() for line in sys.stdin.readlines()]:
    for _ in range(int(steps)):
        rope[0][0] += lookup[dir][0]
        rope[0][1] += lookup[dir][1]
        for i, ((hx, hy), (sx, sy)) in enumerate(zip(rope, rope[1:])):
            if abs(hx - sx) > 1 or abs(hy - sy) > 1:
                rope[i+1][0] += max(-1, min(hx - sx, 1))
                rope[i+1][1] += max(-1, min(hy - sy, 1))
        visited_segment2.add(tuple(rope[1]))
        visited_segment10.add(tuple(rope[-1]))
print(len(visited_segment2))
print(len(visited_segment10))
