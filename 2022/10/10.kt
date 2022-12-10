fun main() {
    val vals = generateSequence(::readlnOrNull).joinToString("\n").replace(" ", "\n").split("\n")
        .map { if (it.length == 4) 0 else it.toInt() }
        .scan(1) {s, e -> s + e}
        .withIndex()
    println(vals.filter { (it.index+1) % 40 == 20 }.sumOf { (it.index+1) * it.value })
    val p2 = vals
        .map { (i, v) -> if (v-1 <= i % 40 && i % 40 <= v+1) "#" else " " }
        .chunked(40)
        .map { it.joinToString("") }
    println(p2.joinToString("\n").trim())
}
