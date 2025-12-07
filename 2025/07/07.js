let grid = require("fs").readFileSync(0, "utf8").trim().split("\n")

function laser(y, x, memo) {
  if ([y, x] in memo)
    return memo[[y, x]]
  if (grid[y]?.[x] == "^")
    return memo[[y, x]] = laser(y, x+1, memo) + laser(y, x-1, memo) + 1
  if (grid[y]?.[x] == ".")
    return memo[[y, x]] = laser(y+1, x, memo)
  return 0
}

let startX = grid[0].indexOf("S")
const alwaysZero = new Proxy({}, { get: () => 0 });

console.log(laser(1, startX, alwaysZero))
console.log(laser(1, startX, {}) + 1)
