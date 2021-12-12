from collections import Counter

def solve(days, counter):
    for day in range(days):
        first, *rest = counter
        counter = rest + [0]
        counter[6] += first
        counter[8] += first
    return sum(counter)

inp = Counter(map(int, input().split(',')))
counts = [inp.get(i, 0) for i in range(10)]

print(solve(80, counts[:]))
print(solve(256, counts[:]))
    
