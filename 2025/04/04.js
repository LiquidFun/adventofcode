let map = require("fs").readFileSync(0, "utf8").trim().split("\n").map(l => l.split(""))
let ADJ = [[0, 1], [1, 0], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
let adj = (y, x) => ADJ.map(([ay, ax]) => map[y + ay]?.[x + ax])

function solve(depth=0) {
  let removed = []
  for (let y = 0; y < map.length; y++)
    for (let x = 0; x < map[0].length; x++)
      if (map[y][x] == "@" && adj(y, x).filter(c => c == "@").length < 4)
        removed.push([y, x])

  removed.forEach(([y,x]) => map[y][x] = 'x')
  if (depth == 0) console.log(removed.length)
  return removed.length != 0 ? solve(depth+1) + removed.length : 0
}
console.log(solve())
