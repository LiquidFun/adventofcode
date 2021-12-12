function solve1(numbers, counts)
    gamma = 0
    for i in counts
        gamma = gamma*2 + (i > length(numbers)/2)
    end
    epsilon = (2^length(counts) - 1) ⊻ gamma
    return gamma * epsilon
end

function solve2(nums, pow)
    function descend_tree(numbers, power, inverse=false)
        if length(numbers) == 1
            return numbers[1]
        end
        matching = 2^power .& numbers 
        sort!(matching)
        sort!(numbers, by=(x) -> x & (2^power))
        
        index = length(numbers) ÷ 2 + 1
        mid = matching[index]
        if (mid == 0) != inverse
            func = x -> (x & 2^power) == 0
        else
            func = x -> !((x & 2^power) == 0)
        end
        filter!(func, numbers)
        return descend_tree(numbers, power-1, inverse)
    end
    return descend_tree(copy(nums), pow, false) * descend_tree(copy(nums), pow, true)
end

function setup()
    counts, numbers = [], []
    for line in readlines()
        for i in eachindex(line)
            if length(counts) < i
                push!(counts, 0)
            end
            counts[i] += '1' == line[i]
        end
        push!(numbers, parse(Int, line, base=2))
    end
    println(solve1(numbers, counts))
    println(solve2(numbers, length(counts) - 1))
end

setup()
