let ranges = (require("fs").readFileSync(0)+"").trim().split(",")
let s1 = s2 = 0;
for (let range of ranges) {
  let [a, b] = range.split("-")
  for (let i = +a; i <= +b; i++) {
    let s = i.toString()
    let size = s.length
    s1 += s.slice(0, size/2) == s.slice(size/2) ? +i : 0
    for (let k = 1; k <= size/2; k++) {
      let set = new Set();
      for (let l = 0; l < size; l += k) {
        set.add(s.slice(l, l+k))
      }
      if (set.size == 1) {
        s2 += i;
        break;
      }
    }
  }
}
console.log(`${s1}\n${s2}`)
