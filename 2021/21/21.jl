function part1(p1, p2, dice=100, goal=1000)
    s1, s2 = 0, 0
    die_value, rolls = 0, 0
    die() = rolls += 1; mod1(die_value += 1, dice)
    roll() = die() + die() + die()
    while s1 < goal || s2 < goal
        s1 += (p1 = mod1(p1 + roll(), 10))
        s1 >= goal && break
        s2 += (p2 = mod1(p2 + roll(), 10))
    end
    return min(s1, s2) * rolls
end

function part2(P1, P2, goal=22)  # Add 1 to goal, since julia is 1 indexed, so dp lookup is different
    dp = zeros(Int64, (goal+11, goal+11, 10, 10, 2))
    dp[1, 1, P1, P2, 1] = 1
    dice = [sum(1 for a=1:3, b=1:3, c=1:3 if a+b+c==s) for s=3:9]
    for s1=1:goal-1, s2=1:goal-1
        for d1=1:10, d2=1:10, add=3:9
            d1a = mod1(d1+add, 10)
            dp[s1+d1a, s2, d1a, d2, 2] += dp[s1, s2, d1, d2, 1] * dice[add-2]
            d2a = mod1(d2+add, 10)
            dp[s1, s2+d2a, d1, d2a, 1] += dp[s1, s2, d1, d2, 2] * dice[add-2]
        end
    end
    dps = sum(dp, dims=(3, 4, 5))
    S1, S2 = 0, 0
    for s1=1:goal+11, s2=1:goal+11
        if max(s1, s2) >= goal
            s1 > s2 ? S1 += dps[s1, s2, 1, 1, 1] : S2 += dps[s1, s2, 1, 1, 1]
        end
    end
    return max(S1, S2)
end

function main()
    p1, p2 = parse.(Int, getindex.(split.(readlines(), ": "), 2))
    println(part1(p1, p2))
    println(part2(p1, p2))
end
main()
