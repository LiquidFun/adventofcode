let coords = require("fs").readFileSync(0, "utf8").trim().split("\n")
  .map(line => line.split(",").map(Number))

let dist = ([[x1,y1,z1], [x2,y2,z2]]) => Math.hypot(x1-x2, y1-y2, z1-z2)

let sortedPairs = coords
  .flatMap((c1, i) => coords.slice(i+1).map(c2 => [c1, c2]))
  .sort((a, b) => dist(a) - dist(b))
  .map(x => x.map(y => coords.indexOf(y)))

let unions = [...Array(1000).keys()].map(i => new Set([i]))

for (let [k, [i, j]] of sortedPairs.entries()) {
  let old = unions[j]
  old.forEach(a => unions[i].add(a))
  unions = unions.map(u => u === old ? unions[i] : u)

  if (k == 1000) {
    console.log(
      [...new Set(unions)]
        .map(u => u.size)
        .sort((a,b) => a-b)
        .slice(-3)
        .reduce((a,b) => a*b))
  }
  if (unions[0].size == 1000) {
    console.log(coords[i][0] * coords[j][0])
    break
  }
}
