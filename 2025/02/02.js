const sum = arr => arr.reduce((a,b) => a + b)

const nums = require("fs").readFileSync(0, "utf8").trim()
  .split(",")
  .map(line => line.split`-`.map(Number))
  .flatMap(([a, b]) => [...Array(b-a+1).keys()].map(i => i+a))

console.log(sum(nums.filter(s => /^(.*)\1$/.test(s))))
console.log(sum(nums.filter(s => /^(.*)\1+$/.test(s))))
