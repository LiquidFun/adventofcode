function main()
    game = readlines() .|> collect
    sy, sx = length(game), length(game[1])
    for iteration in 1:1000
        something_changed = false
        new_pos = Dict()
        for (dir, addx, addy) in [('>', 1, 0), ('v', 0, 1)]
            for y in 1:sy, x in 1:sx
                if game[y][x] == dir
                    ny, nx = mod1(y+addy, sy), mod1(x+addx, sx)
                    if (game[ny][nx] == '.' || dir == 'v' && game[ny][nx] == '>') && (ny, nx) ∉ keys(new_pos) 
                        new_pos[(ny, nx)] = dir
                        something_changed = true
                    else
                        new_pos[(y, x)] = dir
                    end
                end
            end
        end
        game = [[get(new_pos, (y, x), '.') for x in 1:sx] for y in 1:sy]
        !something_changed && return println(iteration)
    end
end
main()
