function main()
    asbin(s) = Int.(collect(s) .== '#') |> join
    lookup = readline() |> asbin
    readline()
    lines = readlines() .|> asbin
    default = '0'
    for iteration in 1:50
        sy, sx = length(lines), length(lines[1])
        atmap(y, x) = (y ∈ 1:sy && x ∈ 1:sx) ? lines[y][x] : default
        expanded = []
        for Y = 0:sy+1
            push!(expanded, [])
            for X = 0:sx+1
                index = parse(Int, join(atmap(Y+y, X+x) for x=-1:1, y=-1:1), base=2)
                push!(expanded[end], lookup[index + 1])
            end
        end
        lines = expanded
        default = (default == '0') ? lookup[1] : lookup[end]
        iteration ∈ [2, 50] && println(lines .|> (line -> line .== '1') |> sum |> sum)
    end
end
main()
