Array.prototype.sumPrint = function () { console.log(this.reduce((a, b) => a + b)) }

const lines = require("fs").readFileSync(0, "utf8").trimEnd().split("\n")
const grid = lines.map(line => line.trim().split(/\s+/))
const ops = grid.pop()
lines.pop()

const transpose = arr => [...arr[0]].map((_, i) => arr.map(row => row[i]))

transpose(grid)
  .map((row, i) => eval(row.join(ops[i])))
  .sumPrint()

transpose(lines)
  .map(row => +row.join(""))
  .join()
  .split(",0,")
  .map((row, i) => eval(row.replaceAll(",", ops[i])))
  .sumPrint()
