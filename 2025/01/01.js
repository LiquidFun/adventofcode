let [s1, s2, a] = [0, 0, 50];

(require("fs").readFileSync(0)+"").trim().split`\n`.forEach(line => {
  let b = a + +line.replace("R", "+").replace("L", "-")
  for (; a != b; a += Math.sign(b-a))
    s2 += a % 100 == 0;
  s1 += a % 100 == 0;
})
console.log(`${s1}\n${s2}`)
