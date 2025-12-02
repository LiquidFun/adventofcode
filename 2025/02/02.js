const range = n => [...Array(n).keys()]
const sum = arr => arr.reduce((a,b) => +a + +b);

const nums = require("fs").readFileSync(0, "utf8").trim()
  .split(",")
  .map(line => line.split`-`.map(Number))
  .flatMap(([a, b]) => range(b-a).map(i => i+a+""))

const isEqual = s => s.slice(s.length/2).repeat(2) == s
const isAnyEqual = s => range(s.length/2|0)
  .some(i => s.slice(0, i+1).repeat(s.length/(i+1)) == s)

console.log(sum(nums.filter(isEqual)))
console.log(sum(nums.filter(isAnyEqual)))
