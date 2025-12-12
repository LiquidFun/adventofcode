let [reqs, ...shapes] = require("fs").readFileSync(0, "utf8").trim().split("\n\n").reverse()

let s1 = 0
reqs.split("\n").forEach(line => {
  let [area, needed] = line.split(": ")
  area = eval(area.replace("x", "*"))
  let sum = eval(needed.replaceAll(" ", "+")) * 9
  s1 += area >= sum
})

console.log(s1)
