const nums = require("fs").readFileSync(0, "utf8").trim()
  .split(",")
  .map(l => l.split`-`.map(Number))
  .flatMap(([a,b]) => [...Array(b-a+1).keys()].map(i => i+a))

console.log(nums.reduce((a,b) => a + b * /^(.*)\1$/.test(b), 0))
console.log(nums.reduce((a,b) => a + b * /^(.*)\1+$/.test(b), 0))
