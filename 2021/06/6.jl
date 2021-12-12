function solve(days, counts)
    for day in 1:days
        first = popfirst!(counts)
        push!(counts, 0)
        counts[7] += first
        counts[9] += first
    end
    return sum(counts)
end

nums = (x -> parse(Int, x)).(split(readline(), ','))
counts = [sum(nums .== i) for i in 0:9]

println(solve(80, copy(counts)))
println(solve(256, copy(counts)))
    
