let s1 = s2 = 0;
require("fs").readFileSync(0, "utf8").trim().split("\n").forEach(line => {
  let best = 0;
  for (let i = 0; i < line.length; i++) {
    for (let j = i+1; j < line.length; j++) {
      best = Math.max(best, +(line[i]+line[j]))
    }
  }
  s1 += best
  let [curr, index] = ["", 0]
  for (let i = 0; i < 12; i++) {
    curr += Math.max(...line.slice(index, line.length-11+i))
    index = line.slice(index).indexOf(curr.at(-1)) + 1 + index
  }
  s2 += +curr
})
console.log(s1)
console.log(s2)
