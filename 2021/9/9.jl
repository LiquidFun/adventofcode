lines = (collect).(readlines())

function is_valid(y, x)
    return 1 <= x <= length(lines[1]) && 1 <= y <= length(lines)
end


function solve_a()
    s = 0
    for y in 1:length(lines)
        for x in 1:length(lines[y])
            good = true
            for (xa, ya) in ((-1, 0), (1, 0), (0, 1), (0, -1))
                if is_valid(y + ya, x + xa)
                    if lines[y + ya][x + xa] <= lines[y][x]
                        good = false
                    end
                end
            end
            if good
                s += parse(Int, lines[y][x]) + 1
            end
        end
    end
    return s
end

function solve_b()
    basins = []
    for Y in 1:length(lines)
        for X in 1:length(lines[Y])
            queue = [(Y, X)]
            s = 0
            while !isempty(queue)
                y, x = popfirst!(queue)
                if lines[y][x] != '9'
                    lines[y][x] = '9'
                    s += 1
                    for (xa, ya) in ((-1, 0), (1, 0), (0, 1), (0, -1))
                        if is_valid(y + ya, x + xa)
                            push!(queue, (y + ya, x + xa))
                        end
                    end
                end
            end
            push!(basins, s)
        end
    end
    return prod(sort(basins)[end-2:end])
end

function main() 
    println(solve_a())
    println(solve_b())
end

main()
