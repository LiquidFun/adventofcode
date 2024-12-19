patterns, designs = open(0).read().split("\n\n")
patterns = patterns.split(", ")

def arrangements(design):
    dp = [1] + [0] * len(design)
    for i in range(len(design)):
        for pattern in patterns:
            if design[i:].startswith(pattern):
                dp[i+len(pattern)] += dp[i]
    return dp[-1]

p = [arrangements(d) for d in designs.split()]
print(sum(map(bool, p)))
print(sum(p))
