function main() 
    arr = collect.(readlines())

    sy, sx = length(arr), length(arr[1])
    is_valid(y, x) = 1 <= y <= sy && 1 <= x <= sx

    flashes = 0
    function flash(y, x)
        if arr[y][x] > '9'
            flashes += 1
            arr[y][x] = '0'
            for (y2, x2) in [(y+a, x+b) for a=-1:1, b=-1:1]
                if is_valid(y2, x2) && arr[y2][x2] != '0'
                    arr[y2][x2] += 1
                    flash(y2, x2)
                end
            end
        end
    end

    total_flashes = 0
    for step in 1:1000
        flashes = 0
        (a -> a .+= 1).(arr)
        for y in 1:sy, x in 1:sx
            flash(y, x)
        end
        total_flashes += flashes
        step == 100 && println(total_flashes)
        flashes == sy * sx && return println(step)
    end
end

main()
