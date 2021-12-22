function solve(data)
    volume(v) = prod(max(0, v[i+1] - v[i] + 1) for i=1:2:5)
    intersection(v1, v2) = [(i % 2 == 1 ? max : min)(v1[i], v2[i]) for i=1:6]
    cubes = []
    for (onoff, nums) in data
        function remove_volume(original, remove)
            # Function to remove one cube from another, by replacing it with up to 6 other cubes
            intersecting = intersection(original, remove)
            volume(intersecting) == 0 && return [original]
            original_divided = []
            add(v) = volume(v) != 0 && push!(original_divided, v)
            x, X, y, Y, z, Z = original
            xi, Xi, yi, Yi, zi, Zi = intersecting
            add([x, xi-1, y, Y, z, Z])
            add([Xi+1, X, y, Y, z, Z])
            add([xi, Xi, y, yi-1, z, Z])
            add([xi, Xi, Yi+1, Y, z, Z])
            add([xi, Xi, yi, Yi, z, zi-1])
            add([xi, Xi, yi, Yi, Zi+1, Z])
            return original_divided
        end
        # Remove the current cube from every previous cube (doesn't matter if on or off)
        !isempty(cubes) && (cubes = reduce(vcat, remove_volume(cube, nums) for cube in cubes))
        # Add the cube if it is turned on
        onoff && push!(cubes, nums)
    end
    # Sum all cubes, since none are intersecting after the previous operations
    return cubes .|> volume |> sum
end
function main()
    extract_ints(str) = parse.(Int, m.match for m in eachmatch(r"-?\d+", str))
    data = split.(readlines()) .|> sp -> (sp[1] == "on", extract_ints(sp[2]))
    data_part1 = filter(nums -> all(i ∈ -50:50 for i=nums[2]), data)

    println(solve(data_part1))
    println(solve(data))
end
main()
