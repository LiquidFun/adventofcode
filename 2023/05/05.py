from sys import stdin

seeds, *mappings = stdin.read().strip().split('\n\n')

seeds = list(map(int, seeds.split()[1:]))
mappings = [[[int(a) for a in m.split()] for m in maps.split('\n')[1:]] for maps in mappings]

def solve(for_ranges):
    min_seed = (1e12, 1e12)
    for for_range in for_ranges:
        for seed in for_range:
            initial_seed = seed
            for mapping in mappings:
                for dst, src, size in mapping:
                    if src <= seed < src + size:
                        seed = dst + (seed - src)
                        break
            if seed < min_seed[1]:
                min_seed = (initial_seed, seed)
    return min_seed

print(solve([[seed] for seed in seeds])[1])

ranges = [range(s, s+count, 100000) for s, count in zip(seeds[0::2], seeds[1::2])]
initial, _ = solve(ranges)
print(solve([range(initial-100000, initial+1)])[1])
