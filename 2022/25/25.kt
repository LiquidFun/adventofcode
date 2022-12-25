import kotlin.math.*
fun Long.pow(e: Int): Long = Math.pow(this.toDouble(), e.toDouble()).toLong()

fun main() {
    var s = generateSequence(::readlnOrNull)
        .map { it.map { "=-012".indexOf(it) - 2 } }
        .sumOf { it.reversed().mapIndexed { i, v -> 5L.pow(i) * v }.sum() }
    var maxPower = log(s.toDouble(), 5.0).toInt()

    var num = ""
    for (power in maxPower downTo 0)
        listOf(-2, -1, 0, 1, 2)
            .minBy { abs(s - 5L.pow(power) * it) }
            .also { s -= 5L.pow(power) * it }
            .also { num += "=-012"[it+2] }
    println(num)
}
