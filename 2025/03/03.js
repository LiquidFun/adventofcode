function best(line, len, curr="", index=0) {
  for (let i = 1; i <= len; i++) {
    curr += Math.max(...line.slice(index, line.length-len+i))
    index += line.slice(index).indexOf(curr.at(-1)) + 1
  }
  return +curr
}

let nums = require("fs").readFileSync(0, "utf8").trim().split("\n")
console.log(nums.map(l => best(l, 2)).reduce((a,b) => a+b))
console.log(nums.map(l => best(l, 12)).reduce((a,b) => a+b))
