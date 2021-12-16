version_sum, bits = 0, join(reverse(digits(parse(BigInt, "1"*readline(), base=16), base=2))[2:end])
function parse_packet(index)  # index is the current index in `bits` string, list of single integer
    take_int(count) = parse(Int, bits[index[1]:((index[1]+=count)-1)], base=2)
    global version_sum += take_int(3)
    id, c = take_int(3), true
    id == 4 && return reduce((a,b)->16a+b, [take_int(4) for _=1:99 if c == 1 && (c = take_int(1)) < 2])
    apply_op(values) = reduce([+, *, min, max, id, >, <, ==][id + 1], values)
    if take_int(1) == 0 && (target_index = take_int(15) + index[1]) != 0
        return [parse_packet(index) for _=1:99 if index[1] < target_index] |> apply_op
    else
        return [parse_packet(index) for _=1:take_int(11)] |> apply_op
    end
end
parse_packet([1]) |> val -> println("$version_sum\n$val") # |> so that sum can be printed before val
