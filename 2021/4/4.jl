bingos = []

scores = []
deleteBingos = []

function removeValue(val)
    for bingo in bingos
        for i in eachindex(bingo)
            if bingo[i] == val
                bingo[i] = 0
            end
        end
    end
end

function checkComplete(num)
    rows = [0 0 0 0 0]
    cols = [0 0 0 0 0]
    for (i, bingo) in enumerate(bingos)
        if any(x -> x == 0, [sum(bingo, dims=1)..., sum(bingo, dims=2)...])
            s = sum(bingo) - sum((x -> x != 0).(bingo))
            push!(scores, s * (num - 1))
            push!(deleteBingos, i)
        end
    end
    return -1
end

function main()
    toInt(x) = parse(Int, x)
    lines = readlines()
    drawn = toInt.(split(lines[1], ",")) .+ 1
    y = 1
    for line in lines[2:end]
        ints = toInt.(split(line)) .+ 1
        if line == ""
            push!(bingos, zeros(Int, (5, 5)))
            y = 1
            continue
        end
        for i in eachindex(ints)
            bingos[end][y, i] = ints[i]
        end
        y += 1
    end
    for num in drawn
        removeValue(num)
        checkComplete(num)
        for i in reverse(deleteBingos)
            deleteat!(bingos, i)
        end
        empty!(deleteBingos)
    end
    println(scores[1])
    println(scores[end])
end

main()
