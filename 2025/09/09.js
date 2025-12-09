let coords = require("fs").readFileSync(0, "utf8").trim().split("\n")
  .map(line => line.split(",").map(Number))

let edges = []
for (let k = 0; k < coords.length; k++) {
  let [x3, y3] = coords[k]
  let [x4, y4] = coords[(k+1)%coords.length]
  edges.push([[x3, y3], [x4, y4]])
}

function intersects([x1, y1], [x2, y2], [x3, y3], [x4, y4]) {
  ;[x1, x2] = [Math.min(x1, x2), Math.max(x1, x2)]
  ;[y1, y2] = [Math.min(y1, y2), Math.max(y1, y2)]
  ;[x3, x4] = [Math.min(x3, x4), Math.max(x3, x4)]
  ;[y3, y4] = [Math.min(y3, y4), Math.max(y3, y4)]
  if (y1 == y2 && y3 == y4) return false
  if (x1 == x2 && x3 == x4) return false
  return y1<y3 && y3<y2 && x3<x1 && x1<x4 || x1<x3 && x3<x2 && y3<y1 && y1<y4
}


let s1 = s2 = 0
for (let i = 0; i < coords.length; i++) {
  for (let j = i+1; j < coords.length; j++) {
    let [x1, y1] = coords[i]
    let [x2, y2] = coords[j]
    ;[x1, x2] = [Math.min(x1, x2), Math.max(x1, x2)]
    ;[y1, y2] = [Math.min(y1, y2), Math.max(y1, y2)]
    let dx = x1-x2, dy = y1-y2
    let curr = (Math.abs(dx)+1) * (Math.abs(dy)+1)
    s1 = Math.max(s1, curr)
    if (curr > s2) {
      let bad = false
      bad ||= edges.some(c => intersects([x1, y1], [x1, y2], ...c))
      bad ||= edges.some(c => intersects([x1, y1], [x2, y1], ...c))
      bad ||= edges.some(c => intersects([x2, y2], [x2, y1], ...c))
      bad ||= edges.some(c => intersects([x2, y2], [x1, y2], ...c))
      bad ||= coords.some(([x, y]) => x1 < x && x < x2 && y1 < y && y < y2)

      if (!bad) { 
        s2 = curr
      }
    }
  }
}

console.log(s1)
console.log(s2)
