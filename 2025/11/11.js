let lines = require("fs").readFileSync(0, "utf8").trim().split("\n")
let adj = new Map(lines
  .map(line => line.split(": "))
  .map(([from, to]) => [from, new Set(to.split(" "))]))
adj.set("out", new Set())

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
  let queue = [start], head = 0
  while (head < queue.length)
    queue.push(...allowed.intersection(adj.get(queue[head++])))
  return queue.filter(node => node == end).length
}

console.log(countPaths("you", "out"))
console.log(countPaths("svr", "fft") * countPaths("fft", "dac") * countPaths("dac", "out"))
