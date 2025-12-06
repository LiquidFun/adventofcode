let lines = require("fs").readFileSync(0, "utf8").split("\n")
lines.pop()
let nums = lines.map(line => line.trim().split(/\s+/))
let ops = nums.pop()

s1 = nums[0].map((_, i) => nums.map(n => +n[i]))
  .map((n, i) => n.reduce((a, b) => ops[i] === '*' ? a * b : a + b))
  .reduce((a, b) => a + b)

console.log(s1)

lines.pop()

s2 = [...lines[0]].map((_, i) => +lines.map(n => n[i]).join(""))
  .join()
  .split(",0,")
  .map((n, i) => eval(n.replaceAll(",", ops[i])))
  .reduce((a, b) => a + b)
console.log(s2)
