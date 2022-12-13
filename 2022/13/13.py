import sys, functools

def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return 0 if a == b else (-1 if a < b else 1)
    a = [a] if isinstance(a, int) else a
    b = [b] if isinstance(b, int) else b
    return ([cmp(*p) for p in zip(a, b) if cmp(*p) != 0] + [cmp(len(a), len(b))])[0]

lists = [eval(a) for a in sys.stdin.read().strip().replace("\n\n", "\n").split("\n")]
print(sum(i for i, pair in enumerate(zip(lists[::2], lists[1::2]), 1) if cmp(*pair) <= 0))

new = sorted(lists + [[[2]], [[6]]], key=functools.cmp_to_key(cmp))
print((new.index([[2]]) + 1) * (new.index([[6]]) + 1))
