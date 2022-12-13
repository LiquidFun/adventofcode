fun main() {
    val vals = generateSequence(::readlnOrNull).joinToString("\n").split(" ", "\n")
         .map { it.toIntOrNull() ?: 0 }
         .scan(1, Int::plus)
         .withIndex()
    println(vals.filter { (it.index+1) % 40 == 20 }.sumOf { (it.index+1) * it.value })
    val p2 = vals
        .map { (i, v) -> if (v-1 <= i % 40 && i % 40 <= v+1) "#" else " " }
        .chunked(40)
        .map { it.joinToString("") }
    println(p2.joinToString("\n").trim())
}
