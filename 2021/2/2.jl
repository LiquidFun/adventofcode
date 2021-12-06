lines = readlines()

function solve(use_aim=false)
    depth, position, aim = 0, 0, 0
    for line in lines
        word, num = split(line)
        num = parse(Int, num)
        if word == "forward"
            position += num
            depth += use_aim ? aim * num : 0
        else 
            if use_aim
                aim += word == "down" ? num : -num
            else
                depth += word == "down" ? num : -num
            end
        end
    end
    return depth * position
end
println(solve(false))
println(solve(true))
