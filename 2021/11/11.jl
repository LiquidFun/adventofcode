function main() 
    lines = readlines()
    arr = [parse(Int, c) for line=lines for c=line]
    arr = reshape(arr, length(lines), length(lines[1]))

    sy, sx = size(arr)
    function is_valid(y, x)
        return 1 <= y <= sy && 1 <= x <= sx
    end

    flashes = 0
    function flash(y, x)
        if arr[y, x] > 9
            flashes += 1
            arr[y, x] = 0
            for (y2, x2) in [(y+a, x+b) for a=-1:1, b=-1:1 if a!=0 || b!=0]
                if is_valid(y2, x2) && arr[y2, x2] != 0
                    arr[y2, x2] += 1
                    flash(y2, x2)
                end
            end
        end
    end

    total_flashes = 0
    for step in 1:1000
        flashes = 0
        arr .+= 1
        for y in 1:sy
            for x in 1:sx
                flash(y, x)
            end
        end
        total_flashes += flashes
        if step == 100
            println(total_flashes)
        end
        if flashes == sy * sx
            println(step)
            break
        end
    end
end

main()
