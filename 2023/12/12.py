from sys import stdin
from functools import cache

@cache
def decide(line, curr, needed, s=0):
    if not line:
        return (needed or (0,)) == (curr,)

    match line[0]:
        case '?':
            s += decide('.' + line[1:], curr, needed)
            s += decide('#' + line[1:], curr, needed)
        case '#' if needed and curr < needed[0]:
            s += decide(line[1:], curr+1, needed)
        case '.' if not needed or curr == 0:
            s += decide(line[1:], 0, needed)
        case '.' if curr == needed[0]:
            s += decide(line[1:], 0, needed[1:])
    return s

s1 = s2 = 0
for line in stdin:
    chars, needed = line.split()
    needed = tuple(int(n) for n in needed.split(","))

    s1 += decide(chars, 0, needed)
    s2 += decide('?'.join([chars] * 5), 0, needed * 5)

print(s1, s2, sep='\n')
