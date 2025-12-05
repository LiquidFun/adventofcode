let [ranges, ingredients] = require("fs").readFileSync(0, "utf8").split("\n\n").map(l => l.split("\n"))

ranges = ranges
  .map(line => line.split("-").map(Number))
  .sort(([a1, b1], [a2, b2]) => a1 - a2)

let s1 = ingredients.map(Number)
  .filter(i => ranges.some(([a, b]) => a <= i && i <= b)).length

let s2 = pa = pb = 0
for (let [a, b] of ranges) {
  if (pa <= a && ++b <= pb) continue
  s2 += b - Math.max(a, pb)
  ;[pa, pb] = [a, b]
}

console.log(`${s1}\n${s2}`)
