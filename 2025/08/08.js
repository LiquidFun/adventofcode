let coords = require("fs").readFileSync(0, "utf8").trim().split("\n")
  .map(line => line.split(",").map(Number))

let deltas = []
for (let i = 0; i < coords.length; i++) {
  for (let j = i+1; j < coords.length; j++) {
    let [x1,y1,z1] = coords[i]
    let [x2,y2,z2] = coords[j]
    let delta = Math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    deltas.push([delta, i, j])
  }
}

deltas.sort(([d1, i1, j1], [d2, i2, j2]) => d1 - d2)
let adj = Array(1000).fill().map(_ => [])

for (let [k, [_, i, j]] of deltas.entries()) {
  adj[i].push(j)
  adj[j].push(i)

  let visited = new Set()

  function floodFill(i) {
    if (visited.has(i)) return 0
    visited.add(i)
    return 1 + adj[i].map(floodFill).reduce((a,b) => a+b, 0)
  }

  if (k == 1000) {
    console.log(
      [...Array(1000).keys()]
        .map(floodFill)
        .sort((a,b) => a-b)
        .slice(-3)
        .reduce((a,b) => a*b))
  }
  if (floodFill(0) == 1000) {
    console.log(coords[i][0] * coords[j][0])
    break
  }
}
