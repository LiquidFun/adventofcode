# Already parsed input file, since this one depends so much on the input.
# Making it general is not very useful.

function main()
    div_z = [1, 1, 1, 1, 26, 1, 26, 26, 1, 1, 26, 26, 26, 26]
    add_x = [14, 13, 13, 12, -12, 12, -2, -11, 13, 14, 0, -12, -13, -6]
    add_w = [8, 8, 3, 10, 8, 8, 8, 5, 9, 3, 4, 9, 2, 7]
    num = 11111111111111
    function calculate_z()
        z, x = 0, 0
        for p=13:-1:0
            i = 14 - p
            w = (num ÷ 10^p) % 10
            x = (z % 26 + add_x[i]) != w
            z = z ÷ div_z[i] * (25x+1) + (w+add_w[i]) * x
            (w == 0 || div_z[i] == 26 && x != 0) && return num += 10^p;
        end
        return z
    end
    solutions = []
    add_sol() = (push!(solutions, num); (num += 1))
    while num < 1e14
        calculate_z() == 0 && add_sol()
    end
    println(solutions[end])
    println(solutions[1])
end
main()

