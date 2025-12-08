let coords = require("fs").readFileSync(0, "utf8").trim().split("\n")
  .map(line => line.split(",").map(Number))

let dist = ([[x1,y1,z1], [x2,y2,z2]]) => Math.hypot(x1-x2, y1-y2, z1-z2)

let sortedPairs = coords
  .flatMap((c1, i) => coords.slice(i+1).map(c2 => [c1, c2]))
  .sort((c1, c2) => dist(c1) - dist(c2))
  .map(pair => pair.map(c => coords.indexOf(c)))

let unions = coords.map((_, i) => new Set([i]))

for (let [i, [u1, u2]] of sortedPairs.entries()) {
  unions[u1].forEach(u => unions[u2].add(u))
  unions[u1].forEach(u => unions[u] = unions[u2])

  if (i == 1000)
    console.log(
      [...new Set(unions)]
        .map(u => u.size)
        .sort((s1, s2) => s1-s2)
        .slice(-3)
        .reduce((s1, s2) => s1*s2))

  if (unions[0].size == 1000)
    process.exit(console.log(coords[u1][0] * coords[u2][0]))
}
