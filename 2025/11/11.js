let lines = require("fs").readFileSync(0, "utf8").trim().split("\n")
let adj = new Map(lines
  .map(line => line.split(": "))
  .map(([from, to]) => [from, to.split(" ")]))
adj.set("out", [])

function descendants(curr, visited = new Set()) {
  if (visited.has(curr)) return
  visited.add(curr)
  adj.get(curr).forEach(next => descendants(next, visited))
  return visited
}

function ancestors(curr) {
  return new Set(adj.keys().filter(node => descendants(node).has(curr)))
}

function countPaths(start, end) {
  let allowed = descendants(start).intersection(ancestors(end))
  let s = 0, head = 0
  let queue = [start]
  while (head < queue.length) {
    let curr = queue[head++]
    s += curr == end
    queue.push(...adj.get(curr).filter(node => allowed.has(node)))
  }
  return s
}

console.log(countPaths("you", "out"))
console.log(countPaths("svr", "fft") * countPaths("fft", "dac") * countPaths("dac", "out"))
