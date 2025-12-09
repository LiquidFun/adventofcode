let coords = require("fs").readFileSync(0, "utf8").trim().split("\n")
  .map(line => line.split(",").map(Number))

let edges = coords.map((c, i) => [c, coords.at(i-1)])

function intersects([x1, y1], [x2, y2], [x3, y3], [x4, y4]) {
  ;[x3, x4] = [Math.min(x3, x4), Math.max(x3, x4)]
  ;[y3, y4] = [Math.min(y3, y4), Math.max(y3, y4)]
  return y1<y3 && y3<y2 && x3<x1 && x1<x4 || x1<x3 && x3<x2 && y3<y1 && y1<y4
}

let s1 = s2 = 0
for (let [X1, Y1] of coords) {
  for (let [x2, y2] of coords) {
    ;[x1, x2] = [Math.min(X1, x2), Math.max(X1, x2)]
    ;[y1, y2] = [Math.min(Y1, y2), Math.max(Y1, y2)]
    let curr = (x2-x1+1) * (y2-y1+1)
    s1 = Math.max(s1, curr)
    if (curr > s2) {
      let bad = coords.some(([x, y]) => x1 < x && x < x2 && y1 < y && y < y2)
        || edges.some(c => intersects([x1, y1], [x1, y2], ...c))
        || edges.some(c => intersects([x1, y1], [x2, y1], ...c))
        || edges.some(c => intersects([x2, y1], [x2, y2], ...c))
        || edges.some(c => intersects([x1, y2], [x2, y2], ...c))

      if (!bad) s2 = curr
    }
  }
}

console.log(s1)
console.log(s2)
