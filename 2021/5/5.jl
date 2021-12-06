function solve(lines, allow_diagonals)
    map = zeros(Int, (1001, 1001))
    for line in lines
        from, to = split(line, " -> ")
        toCoords(x) = (a -> parse(Int, a)).(split(x, ","))
        from = toCoords(from) .+ 1  # Shift all by one, so that Julia indices would work
        to = toCoords(to) .+ 1
        if any(from .== to) || allow_diagonals
            while from != to
                map[from[2], from[1]] += 1
                from += (to .> from) - (to .< from)
            end
            map[from[2], from[1]] += 1
        end
    end
    return sum(map .>= 2)
end

function main() 
    lines = readlines()
    println(solve(lines, false))
    println(solve(lines, true))
end

main()
