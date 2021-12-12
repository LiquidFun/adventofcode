function solve(connections, use_twice=false)

    paths = Vector()
    visited = Set()
    function dfs(curr, can_still_use_twice=false, path=Vector())
        key = curr * (curr in visited ? "2" : "")
        push!(path, curr)
        if lowercase(curr) == curr
            push!(visited, key)
        end
        if curr == "end"
            push!(paths, join(path, ','))
        else
            for connection in connections[curr]
                if connection ∉ visited
                    dfs(connection, can_still_use_twice, copy(path))
                elseif can_still_use_twice && connection ∉ ["start", "end"]
                    dfs(connection, false, copy(path))
                end
            end
        end
        delete!(visited, key)
    end

    dfs("start", use_twice)
    return length(paths)
end

function main()
    connections = Dict()
    for line in readlines()
        from, to = split(line, '-')
        push!(get!(connections, from, Vector()), to)
        push!(get!(connections, to, Vector()), from)
    end
    println(solve(connections))
    println(solve(connections, true))
end

main()
