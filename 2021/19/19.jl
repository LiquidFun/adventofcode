function main()
    scanners = []
    for line in readlines()
        if occursin('s', line)
            #= isempty(scanners) ? nothing : scanners[end] = hcat(scanners[end]...) =#
            push!(scanners, [])
        elseif occursin(',', line)
            push!(scanners[end], [parse.(Int, split(line, ','))...])
        end
    end
    display(scanners[2])
    println()
    println()
    queue = Vector([1])
    coords_lookup = Dict(1 => [0, 0, 0])
    while !isempty(queue)
        curr_scanner = pop!(queue)
        for s2i in eachindex(scanners)
            s2i ∈ keys(coords_lookup) && continue
            s, s2 = scanners[curr_scanner], scanners[s2i]
            best = 0
            perms = [(a, b, c) for a=1:3, b=1:3, c=1:3 if a != b != c != a]
            for (a, b, c) ∈ perms, nx ∈ [-1, 1], ny ∈ [-1, 1], nz ∈ [-1, 1]
                diff_dict = Dict()
                s2mod = s2 .|> (vec -> vec .* [nx, ny, nz]) .|> (vec -> [vec[a], vec[b], vec[c]])
                #= s2mod = s2 .|> (vec -> vec .* [nx, ny, nz]) .|> (vec -> vcat(vec[1+r:end], vec[1:r])) =#
                for s2vec in s2mod
                    diffs = s .|> svec -> svec .- s2vec
                    for diff in diffs
                        diff_dict[diff] = get!(diff_dict, diff, 0) + 1
                        if diff_dict[diff] >= 12
                            println(diff)
                            #= is = [a==1 ? 1 : b==1 ? 2 : 3, b==2 ? 2 : a==2 ? 1 : 3, c==3 ? 3 : a==3 ? 1 : 2] =#
                            #= println((a, b, c), is) =#
                            #= diff_reverse = diff |> (v -> v .* [nx, ny, nz])  |> (v -> [v[is[1]], v[is[2]], v[is[3]]]) =# 
                            coords_lookup[s2i] = coords_lookup[curr_scanner] .+ diff
                            s2i ∉ queue && push!(queue, s2i)
                        end
                    end
                end
                #= 1 2 3 =#
                #= 3 1 2 -> =# 
                #= 2 3 1 =#

                #= 1 3 2 =#
                #= 1 3 2 =# 
                best = max(best, diff_dict |> values |> maximum)
                #= display(diff_dict) =#
                #= println() =#
                #= println(maximum(values(diff_dict))) =#
                #= println(sum(values(diff_dict))) =#
            end
            if best >= 12
                println("Scanner $(curr_scanner-1) and $(s2i-1) share $best beacons")
                #= println("$(si-1) $(s2i-1)") =#
            end
        end
    end
    points = Set()
    for i in eachindex(scanners)
        for point in scanners[i] .|> vec -> vec .+ coords_lookup[i]
            push!(points, point)
        end
    end
    println(length(points))
    display(coords_lookup)
end
main()
