let lines = require("fs").readFileSync(0, "utf8").trim().split("\n")

let map = new Map()
for (let line of lines) {
  let [from, ...to] = line.split(/:? /)
  map.set(from, to)
}

console.log(map.get("you"))
//console.log(map)

let s1 = 0

function descendants(curr, visited = new Set()) {
  if (visited.has(curr)) return
  visited.add(curr)
  map.get(curr)?.forEach(next => descendants(next, visited))
  return visited
}

function ancestors(curr) {
  return new Set(map.keys().filter(node => descendants(node).has(curr)))
}

function countPaths(start, end, ...alsoIgnore) {
  let allowed = descendants(start).intersection(ancestors(end))
  allowed.add(end)
  let s = 0
  let queue = [start]
  let head = 0
  while (head < queue.length) {
    if (queue.length > 10_000_000) {
      queue = queue.slice(head)
      head = 0
    }
    let curr = queue[head++]
    if (curr == end) {
      s++
      continue
    }
    //if (queue.length%10000 == 0) console.log(queue.length)
    for (let next of (map.get(curr))) {
      if (allowed.has(next))
        queue.push(next)
    }
  }
  console.log(s)
  return s
}

let svr2fft = countPaths("svr", "fft", "dac")
//let svr2dac = countPaths("svr", "dac", "fft")
//let dac2fft = countPaths("dac", "fft")
let fft2dac = countPaths("fft", "dac")
//let fft2out = countPaths("fft", "out")
let dac2out = countPaths("dac", "out")

console.log(svr2fft * fft2dac * dac2out)


function countPaths2(start, end) {
  let queue = [[start]]
  let head = 0
  while (head < queue.length) {
    let [front, ...rest] = queue[head++]
    if (front == "out") {
      s1 += rest.includes("dac") && rest.includes("fft")
      continue
    }
    //console.log(front)
    for (let next of (map.get(front))) {
      queue.push([next, front, ...rest])
    }
  }
  console.log(s1)
}
