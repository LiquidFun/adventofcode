x1, x2, y1, y2 = [parse(Int, m.match) for m in eachmatch(r"-?\d+", readline())]
count = 0
function simulate(yspeed, xspeed)
    x, y, maxy = 0, 0, 0
    while x <= x2 && y >= y1
        y, x = y + (yspeed -= 1), x + (xspeed -= xspeed > 0)
        maxy = max(y, maxy)
        x ∈ x1:x2 && y ∈ y1:y2 && (global count += 1) > 0 && return maxy
    end
    return 0
end
maximum(simulate(ys, xs) for ys=y1:200, xs=1:x2+1) |> m -> println("$m\n$count")
