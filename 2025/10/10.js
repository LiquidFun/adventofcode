const { init } = require('z3-solver');

let lines = require("fs").readFileSync(0, "utf8").trim().split("\n")

function part1(target, buttons) {
  let visited = new Set([0])
  let queue = [[0, 0]]
  let head = 0
  while (queue) {
    let [curr, dist] = queue[head++]
    if (curr == target) return dist
    for (let button of buttons) {
      if (!visited.has(curr ^ button)) {
        visited.add(curr)
        queue.push([curr ^ button, dist+1])
      }
    }
  }
}

async function part2(joltages, buttons) {
  const { Context } = await init();
  const Z3 = new Context('main');

  const opt = new Z3.Optimize();
  const bs = buttons.map((_, i) => Z3.Int.const('b'+i))
  let sum = arr => arr.reduce((a,b) => b.add(a))

  joltages.map((joltage, jIdx) => {
    opt.add(sum(bs.filter((_, i) => buttons[i].includes(jIdx))).eq(joltage))
  })

  bs.map(b => opt.add(b.ge(0)))
  opt.minimize(sum(bs))
  await opt.check()
  let model = opt.model()
  return Number(model.eval(sum(bs)))
}

let s1 = 0
let promises = []
for (let line of lines) {
  let [target, ...buttons] = line.split(" ")
  let joltage = buttons.pop().slice(1, -1).split(",").map(Number)
  target = parseInt(target.slice(1, -1).split(".").reverse().join("0").replaceAll("#", "1"), 2)
  let toNum = n => eval(n.replace("(", "(2**").replaceAll(",", "+2**"))
  s1 += part1(target, buttons.map(toNum))

  let mapped = buttons.map(button => button.slice(1, -1).split(",").map(Number))
  promises.push(part2(joltage, mapped))
}

console.log(s1)
Promise.all(promises).then(result => console.log(result.reduce((a, b) => a+b)))
