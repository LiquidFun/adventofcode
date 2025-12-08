let coords = require("fs").readFileSync(0, "utf8").trim().split("\n")
  .map(line => line.split(",").map(Number))

let dist = ([[x1,y1,z1], [x2,y2,z2]]) => Math.hypot(x1-x2, y1-y2, z1-z2)

let deltas = coords
  .flatMap((c1, i) => coords.slice(i+1).map(c2 => [c1, c2]))
  .sort((a, b) => dist(a) - dist(b))
  .map(x => x.map(y => coords.indexOf(y)))

let adj = Array(1000).fill().map(_ => [])

for (let [k, [i, j]] of deltas.entries()) {
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
