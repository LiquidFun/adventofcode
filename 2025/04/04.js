let map = require("fs").readFileSync(0, "utf8").trim().split("\n")
let ADJ = [[0, 1], [1, 0], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
let adj = (y, x) => ADJ.map(([ay, ax]) => (map[y + ay] || [])[x + ax])

let s2 = 0
for (let it = 0; ; it++) {
  let removed = []
  for (let y = 0; y < map.length; y++) {
    for (let x = 0; x < map[0].length; x++) {
      let s = adj(y, x).filter(c => c == "@").length
      if (map[y][x] == "@" && s < 4)
        removed.push([y, x])
    }
  }
  s2 += removed.length
  for (let [y, x] of removed)
    map[y] = map[y].slice(0, x) + 'x' + map[y].slice(x + 1)
  if (it == 0) console.log(removed.length)
  if (removed.length == 0) break
}
console.log(s2)
