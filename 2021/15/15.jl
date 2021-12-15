using DataStructures
lines = readlines() .|> collect
small = [parse(Int, lines[y][x]) for y=1:length(lines), x=1:length(lines[1])]
large = reduce(hcat, [(small .- 1 .+ i) .% 9 .+ 1 for i=0:4])
large = reduce(vcat, [(large .- 1 .+ i) .% 9 .+ 1 for i=0:4])

function solve(field)
    sy, sx = size(field)
    queue = PriorityQueue((1, 1) => 0)
    cost = Dict((1, 1) => 0)
    while !isempty(queue)
        (y, x), prio = dequeue_pair!(queue)
        cost[(y, x)] = prio
        y == sy && x == sx && return prio
        for (y2, x2) in eachrow([-1 0; 1 0; 0 -1; 0 1] .+ [y x])
            if 1 <= y2 <= sy && 1 <= x2 <= sx && (y2, x2) ∉ keys(cost)
                newval, currval = (prio + field[y2, x2]), get(queue, (y2, x2), typemax(Int))
                newval < currval && (queue[(y2, x2)] = newval)
            end
        end
    end
end

println(solve(small))
println(solve(large))
