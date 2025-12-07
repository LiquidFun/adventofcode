grid = require("fs").readFileSync(0, "utf8").trim().split("\n").map(line => line.split(""))

function solve(quantum) {
  let memo = {}

  function descend(y, x) {
    let key = [y, x]
    if (key in memo)
      return quantum ? memo[key] : 0
    if (grid[y]?.[x] == "^")
      return memo[key] = descend(y, x+1) + descend(y, x-1) + 1
    if (grid[y]?.[x] == ".")
      return memo[key] = descend(y+1, x)
    return 0
  }
  let startX = grid[0].indexOf("S")
  console.log(descend(1, startX) + quantum)
}

solve(false)
solve(true)
