dp, lookup = Dict(), Dict()
function search_dp(key)
    key in keys(dp) && return dp[key]
    return dp[key] = sum(search_dp((key[1] - 1, letters)) for letters in lookup[key[2]])
end
template = readline(); readline()
for (from, to) in readlines() .|>  line -> split(line, " -> ")
    dp[(1, from)] = [count(==(c), from[1] * to) for c in 'A':'Z']
    lookup[from] = (from[1] * to, to * from[2])
end
function solve(for_step)
    occ = sum(search_dp((for_step, a * b)) for (a, b) in zip(template, template[2:end]))
    occ[template[end] - 'A' + 1] += 1
    return maximum(occ) - minimum(filter(!=(0), occ))
end
println(solve(10))
println(solve(40))
