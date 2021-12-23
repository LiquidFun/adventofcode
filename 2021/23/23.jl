# Pretty slow solution. Both part 1 and 2 take around 20 seconds
using DataStructures
function solve(game::Vector{Vector{Char}})
    game = [line[2:end-1] for line in game[2:end-1]]
    sy, sx = length(game), length(game[1])
    depth = sy - 1
    nswe = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    adjacent(y, x) = [(y+ya, x+xa) for (ya, xa)=nswe if (y+ya)∈1:sy && (x+xa)∈1:sx]
    is_legal(yx) = occursin(game[yx[1]][yx[2]], ".ABCD")
    adjacent_legal = Dict()
    legal_coords = []
    target_lookup = Dict(a => ("."^i * a^(depth-i) for i=1:depth) for a in "ABCD")
    allowed_lookup = [Set(), Set((1, xa) for xa in (1, 2, 4, 6, 8, 10, 11))]

    for y=1:sy, x=1:sx
        if is_legal((y, x))
            adjacent_legal[(y, x)] = filter(is_legal, adjacent(y, x))
            (game[y][x] != '.' || game[y+1][x] == '#') && push!(legal_coords, (y, x))
        end
    end
    state_queue = PriorityQueue(game => 0)
    states_visited = Set{UInt64}()
    while !isempty(state_queue)
        state, cost = dequeue_pair!(state_queue)
        push!(states_visited, hash(state))
        if all(state[ys][xs] == ('A'+(xs-3)÷2) for (ys, xs) in legal_coords[end-(4*depth-1):end])
            return cost
        end
        for (y, x) in legal_coords
            if (a = state[y][x]) != '.'
                target = target_lookup[a]
                allowed = allowed_lookup[(y != 1) + 1]
                target_x = 3 + 2(a - 'A')
                slot = join(state[2+d][target_x] for d=0:depth-1)
                slot_pos = slot ∈ target ? (1 + sum(collect(slot) .== '.'), target_x) : (0, 0)
                isempty(allowed) && slot_pos == (0, 0) && continue
                visited = Set{Tuple{Int64, Int64}}()
                queue = Queue{Tuple{Int64, Int64, Int64}}()
                enqueue!(queue, (cost, y, x))
                while !isempty(queue)
                    new_cost, yc, xc = dequeue!(queue)
                    if slot_pos == (yc, xc) || (yc, xc) ∈ allowed
                        new_state = deepcopy(state)
                        new_state[yc][xc] = a
                        new_state[y][x] = '.'
                        if hash(new_state) ∉ states_visited
                            state_queue[new_state] = min(new_cost, get(state_queue, new_state, typemax(Int)))
                        end
                    end
                    push!(visited, (yc, xc))
                    for (ya, xa) in adjacent_legal[(yc, xc)]
                        if state[ya][xa] == '.' && (ya, xa) ∉ visited
                            adj_cost = new_cost + (10^(a - 'A'))
                            push!(visited, (ya, xa))
                            enqueue!(queue, (adj_cost, ya, xa))
                        end
                    end
                end
            end
        end
    end
end

function main()
    game = readlines() .|> collect
    println(solve(game))

    insert!(game, length(game)-1, collect("  #D#C#B#A#  "))
    insert!(game, length(game)-1, collect("  #D#B#A#C#  "))
    println(solve(game))
end
main()

