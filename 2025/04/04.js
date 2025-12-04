let map = require("fs").readFileSync(0, "utf8").trim().split("\n")
let adj = [[0, 1], [1, 0], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

let s1 = s2 = 0
for (let it = 0; ; it++) {
  s1 = 0
  let removed = []
  for (let y = 0; y < map.length; y++) {
    for (let x = 0; x < map[0].length; x++) {
      let s = 0
      for (let [ax, ay] of adj) {
        s += (map[y + ay] || [])[x + ax] == "@"
      }
      if (map[y][x] == "@") {
        if (s < 4) removed.push([y, x])
        s1 += s < 4
      }
    }
  }
  s2 += s1
  for (let [y, x] of removed) map[y] = map[y].slice(0, x) + 'x' + map[y].slice(x + 1)
  if (it == 0) console.log(s1)
  if (s1 == 0) break
}
console.log(s2)
