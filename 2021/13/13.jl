function main()
    coords = Set()
    first_fold = true
    for line in readlines()
        if ',' in line
            x, y = split(line, ',') .|> x -> parse(Int, x)
            push!(coords, (y, x))
        elseif '=' in line
            fold_is_x = occursin("x=", line)
            fold_val = parse(Int, split(line, '=')[2])
            new_coords = Set()
            for (y, x) in coords
                fold_x = fold_is_x ? min(0, fold_val - x) * 2 : 0
                fold_y = fold_is_x ? 0 : min(0, fold_val - y) * 2
                push!(new_coords, (y + fold_y, x + fold_x))
            end
            coords = new_coords
            first_fold && length(coords) |> println
            first_fold = false
        end
    end
    y_max, x_max = maximum(coords) .+ 1
    field = [collect(" " ^ x_max) for _ in 1:y_max]
    for (y, x) in coords
        field[y + 1][x + 1] = '#'
    end
    field .|> join .|> println
end

main()
