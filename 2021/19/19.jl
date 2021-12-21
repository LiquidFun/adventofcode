function main()
    scanners = []
    for line in readlines()
        if occursin('s', line)
            push!(scanners, [])
        elseif occursin(',', line)
            push!(scanners[end], [parse.(Int, split(line, ','))...])
        end
    end
    queue = [scanners[1]]
    coords_lookup = Dict(scanners[1] => [0, 0, 0])
    while !isempty(queue)
        curr_scanner = pop!(queue)
        for other_scanner in scanners
            other_scanner ∈ keys(coords_lookup) && continue
            rotations = [(a, b, c) for a=1:3, b=1:3, c=1:3 if a != b != c != a]
            flips = [(nx, ny, nz) for nx=[-1, 1], ny=[-1, 1], nz=[-1, 1]]
            function try_all_perms()
                for (r1, r2, r3) ∈ rotations, flip ∈ flips
                    other_permuted = other_scanner .|> (v -> v .* flip) .|> (v -> [v[r1], v[r2], v[r3]])
                    diff_counter = Dict()
                    for other_vec in other_permuted
                        differences = curr_scanner .|> curr_vec -> curr_vec .- other_vec
                        for diff in differences
                            if (diff_counter[diff] = get!(diff_counter, diff, 0) + 1) >= 12
                                coords_lookup[other_scanner] = diff
                                for i in eachindex(other_scanner)
                                    other_scanner[i] = other_permuted[i] .+ diff
                                end
                                other_scanner ∉ queue && push!(queue, other_scanner)
                                return
                            end
                        end
                    end
                end
            end
            try_all_perms()
        end
    end
    println(length(Set(vcat(scanners...))))
    println([sum(abs.(a .- b)) for a=values(coords_lookup), b=values(coords_lookup)] |> maximum)
end
main()
