Array.prototype.sumPrint = function () { console.log(this.reduce((a, b) => a + b)) }

const lines = require("fs").readFileSync(0, "utf8").trimEnd().split("\n")
const nums = lines.map(line => line.trim().split(/\s+/))
const ops = nums.pop()
lines.pop()

const transpose = arr => [...arr[0]].map((_, i) => arr.map(n => n[i]))

transpose(nums)
  .map((n, i) => eval(n.join(ops[i])))
  .sumPrint()

transpose(lines)
  .map(l => +l.join(""))
  .join()
  .split(",0,")
  .map((n, i) => eval(n.replaceAll(",", ops[i])))
  .sumPrint()
