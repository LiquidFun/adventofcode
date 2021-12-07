function solve(nums, use_growing=false)
    counter = zeros(Int, maximum(nums) + 1)
    grow = copy(counter)
    for num in nums
        counter[num + 1] += 1
    end
    s = 0
    while length(counter) > 1
        front, back = counter[1] + grow[1], counter[end] + grow[end]
        if front < back
            counter[2] += counter[1]
            popfirst!(counter)
            if use_growing
                popfirst!(grow)
                grow[1] = front
            end
            s += front
        else
            counter[end-1] += counter[end]
            pop!(counter)
            if use_growing
                pop!(grow)
                grow[end] = back
            end
            s += back
        end
    end
    return s
end

function main()
    nums = (x -> parse(Int, x)).(split(readlines()[1], ','))
    println(solve(nums, false))
    println(solve(nums, true))
end

main()
