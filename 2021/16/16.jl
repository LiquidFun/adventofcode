
function main()
    codes = parse.(Int, collect(readline()), base=16)
    bits = join(hcat(reverse.(digits.(codes, base=2, pad=4))...))
    version_sum = 0
    function parse_packet(s)
        take_bits(count) = bits[s:((s+=count)-1)]
        take_int(count) = parse(Int, take_bits(count), base=2)
        version = take_int(3)
        id = take_int(3)
        version_sum += version
        value = 0
        if id == 4
            bin_num = ""
            while true
                is_last_block = take_int(1) == 0
                bin_num *= take_bits(4)
                is_last_block && break
            end
            value = parse(Int, bin_num, base=2)
        else
            length_type_id = take_int(1)
            length_data = take_int(length_type_id == 1 ? 11 : 15)
            values = []
            if length_type_id == 0
                target_s = s + length_data
                while s < target_s
                    s, val = parse_packet(s)
                    push!(values, val)
                end
            else
                for packet in 1:length_data
                    s, val = parse_packet(s)
                    push!(values, val)
                end
            end
            id == 0 && (value = sum(values))
            id == 1 && (value = prod(values))
            id == 2 && (value = minimum(values))
            id == 3 && (value = maximum(values))
            id == 5 && (value = values[1] > values[2])
            id == 6 && (value = values[1] < values[2])
            id == 7 && (value = values[1] == values[2])
        end
        return s, value
    end
    s, val = parse_packet(1)
    println(version_sum)
    println(val)
end
main()
