nums = (x -> parse(Int, x)).(readlines())
solve(dist) = sum(a < b for (a, b) in zip(nums, nums[dist:end]))
println(solve(2))
println(solve(4))
