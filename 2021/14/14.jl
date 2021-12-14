dp = Dict()
lookup = Dict()
function search_dp(count, letters)
    (count, letters) in keys(dp) && return dp[(count, letters)]
    left, right = letters[1] * lookup[letters], lookup[letters] * letters[2]
    return dp[(count, letters)] = search_dp(count - 1, left) + search_dp(count - 1, right)
end
first = readline()
for line in filter(x -> occursin("->", x), readlines())
    from, to = split(line, " -> ")
    dp[(1, from)] = [sum(c .== collect(from[1] * to)) for c in 'A':'Z']
    lookup[from] = to
end
function solve(for_step)
    occ = sum(search_dp(for_step, a * b) for (a, b) in zip(first, first[2:end]))
    occ[first[end] - 'A' + 1] += 1
    return maximum(occ) - minimum(filter(!=(0), occ))
end
println(solve(10))
println(solve(40))
