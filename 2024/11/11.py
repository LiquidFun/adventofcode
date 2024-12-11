from collections import Counter

def blink(counts, blinks):
    for _ in range(blinks):
        for n, occ in list(counts.items()):
            s = str(n)
            if n == 0:
                counts[1] += occ
            elif len(s) % 2 == 0:
                counts[int(s[:len(s)//2])] += occ
                counts[int(s[len(s)//2:])] += occ
            else:
                counts[n * 2024] += occ
            counts[n] -= occ
    return counts

counts = Counter([int(a) for a in input().split()])
print(sum(blink(counts, 25).values()))
print(sum(blink(counts, 50).values()))

