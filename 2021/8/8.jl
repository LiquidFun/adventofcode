function solve(digits, actual, easy)
    if easy
        return sum((x -> x in [2, 3, 4, 7]).((length).(actual)))
    else
        # Idea: 
        #   find '1', '4', '7' and '8' through number of segments
        #
        #   find '3' by seeing which number with 5 segments has 2 in common with '1'
        #   find '2' and '5' by taking remaining 5 segment numbers, '5' has 3 segments in common with '4'
        #
        #   find '6' by seeing which number with 6 segments has 1 in common with '1'
        #   find '0' and '9' by taking remaining 6 segment numbers, '9' has 4 segments in common with '4'
        #
        sort_internal(x) = join(sort(collect(x)))
        ds = (sort_internal).(digits)
        as = (sort_internal).(actual)

        sort!(ds, by=length)
        zero, one, two, three, four, five, six, seven, eight, nine = "abcdefghij"
        one, seven, four, eight = ds[1], ds[2], ds[3], ds[end]
        for i in 4:6
            if length(intersect(ds[i], one)) == 2
                three = ds[i]
                two = ds[(i - 3) % 3 + 4]
                five = ds[(i - 2) % 3 + 4]
            end
        end
        if length(intersect(two, four)) == 3
            two, five = five, two
        end
        for i in 7:9
            if length(intersect(ds[i], one)) == 1
                six = ds[i]
                zero = ds[(i - 6) % 3 + 7]
                nine = ds[(i - 5) % 3 + 7]
            end
        end
        if length(intersect(zero, four)) == 4
            zero, nine = nine, zero
        end
        lookup = [zero, one, two, three, four, five, six, seven, eight, nine]

        ans = 0
        for a in as
            ans = 10ans + (findfirst(isequal(a), lookup) - 1)
        end
        return ans
    end
end

# 2 -> 1
# 3 -> 7
# 4 -> 4
# 5 -> 2, 3, 5
# 6 -> 6, 9, 0
# 7 -> 8

function main()
    s_easy = 0
    s_hard = 0
    for line in readlines()
        digits, actual = split(strip(line), " | ")
        digits = split(digits)
        actual = split(actual)
        s_easy += solve(digits, actual, true)
        s_hard += solve(digits, actual, false)
    end
    println(s_easy)
    println(s_hard)
end

main()
