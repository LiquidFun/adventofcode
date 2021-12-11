function main()
    score = Dict(')' => 3, ']' => 57, '}' => 1197, '>' => 25137)
    opposite = Dict(')' => '(', ']' => '[', '}' => '{', '>' => '<')
    points = Dict('(' => 1, '[' => 2, '{' => 3, '<' => 4)
    s = 0
    scores = Vector{Int}()
    for line in readlines()
        stack = Vector{Char}()
        corrupted = false
        for char in line
            if char in "([{<"
                push!(stack, char)
            else
                last = pop!(stack)
                if opposite[char] != last
                    s += score[char]
                    corrupted = true
                    break
                end
            end
        end
        if !corrupted
            curr = 0
            while !isempty(stack)
                curr = 5curr + points[pop!(stack)]
            end
            if curr != 0
                push!(scores, curr)
            end
        end
    end
    println(s)
    sort!(scores)
    println(scores[(length(scores)+1)÷2])
end

main()
