lookup, _, lines... = readlines() .|> s -> (Int.(collect(s) .== '#') |> join)
default = '0'
for iteration in 1:50
    sy, sx = length(lines), length(lines[1])
    atmap(y, x) = (y ∈ 1:sy && x ∈ 1:sx) ? lines[y][x] : default
    get_index(Y, X) = parse(Int, join(atmap(Y+y, X+x) for x=-1:1, y=-1:1), base=2) + 1
    global lines = [[lookup[get_index(Y, X)] for X=0:sx+1] for Y=0:sy+1]
    global default = (default == '0') ? lookup[1] : lookup[end]
    iteration ∈ [2, 50] && println(lines .|> (line -> line .== '1') |> sum |> sum)
end
