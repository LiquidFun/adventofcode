mutable struct Tree
    parent
    left
    right
end

function Tree(parent)
    Tree(parent, nothing, nothing)
end

function Base.show(io::IO, tree::Tree)
    tree isa Number && return print(tree)
    print("[")
    print(tree.left)
    print(",")
    print(tree.right)
    print("]")
end

function make_tree(list, parent=nothing)
    list isa Number && return list
    curr = Tree(parent)
    curr.left = make_tree(list[1], curr)
    curr.right = make_tree(list[2], curr)
    return curr
end

function explode(curr, left_leaf, right_leaf)
    if left_leaf != nothing
        left_leaf.right isa Number ? left_leaf.right += curr.left : left_leaf.left += curr.left
    end
    if right_leaf != nothing
        right_leaf.left isa Number ? right_leaf.left += curr.right : right_leaf.right += curr.right
    end
    if curr.parent.left === curr
        curr.parent.left = 0
    else
        curr.parent.right = 0
    end
    return true
end

function find_leaves(curr, depth=0)
    curr isa Number && return []
    mid = curr.left isa Number || curr.right isa Number ? [(depth, curr)] : []
    vcat(find_leaves(curr.left, depth+1), mid, find_leaves(curr.right, depth+1))
end

function find_next_explode(tree)
    leaves = vcat([(0, nothing)], find_leaves(tree), [(0, nothing)])
    for i in eachindex(leaves)
        if leaves[i][1] >= 4 && leaves[i][2].left isa Number && leaves[i][2].right isa Number
            return explode(leaves[i][2], leaves[i-1][2], leaves[i+1][2])
        end 
    end
    return false
end

function find_next_split(tree)
    found_split = false
    should_split(num) = num isa Number && num > 9
    function split_descend(curr)
        split_up(num) = Tree(curr, num ÷ 2, num - num ÷ 2)
        curr isa Number && return false
        found_split && return true
        should_split(curr.left) && (curr.left = split_up(curr.left)) != 1 && return found_split = true
        split_descend(curr.left) && return true
        should_split(curr.right) && (curr.right = split_up(curr.right)) != 1 && return found_split = true
        split_descend(curr.right) && return true
        return false
    end
    return split_descend(tree)
end

function reduce_tree(tree)
    i = 0
    while true
        find_next_explode(tree) && continue
        find_next_split(tree) && continue
        return tree
    end
end

function merge_trees(left_tree, right_tree)
    new_root = Tree(nothing)
    left_tree.parent = new_root
    right_tree.parent = new_root
    new_root.left = left_tree
    new_root.right = right_tree
    return new_root
end

function add_trees(tree1, tree2)
    merge_trees(tree1, tree2) |> reduce_tree
end

function magnitude(tree)
    tree isa Number && return tree
    return 3magnitude(tree.left) + 2magnitude(tree.right)
end

function solve_part1(trees)
    curr = trees[1]
    for next in trees[2:end]
        merged = merge_trees(curr, next)
        curr = reduce_tree(merged)
    end
    println(magnitude(curr))
end

function solve_part2(trees)
    best = 0
    for t1 in trees, t2 in trees
        if !(t1 == t2) 
            best = max(best, add_trees(deepcopy(t1), deepcopy(t2)) |> magnitude)      
        end
    end
    println(best)
end

function main()
    trees = readlines() .|> Meta.parse .|> eval .|> make_tree
    solve_part1(deepcopy(trees))
    solve_part2(deepcopy(trees))
end

main()
