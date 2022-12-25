import kotlin.math.*
fun pow5(e: Int): Long = 5.0.pow(e.toDouble()).toLong()

fun main() {
    var s = generateSequence(::readlnOrNull)
        .map { it.map { "=-012".indexOf(it) - 2 } }
        .sumOf { it.reversed().mapIndexed { i, v -> pow5(i) * v }.sum() }

    for (power in log(1.0 * s, 5.0).toInt() downTo 0)
        (-2..2)
            .minBy { abs(s - pow5(power) * it) }
            .also { s -= pow5(power) * it }
            .also { print("=-012"[it+2]) }
}
