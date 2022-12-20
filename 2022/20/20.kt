import java.util.Collections.swap

fun MutableList<IndexedValue<Long>>.simulate(times: Int, decryptKey: Long = 1L) {
    for (index in 0 until size * times) {
        var i = indexOfFirst { it.index == index % size }
        var v = (this[i].value * decryptKey % (size-1)).toInt()
        repeat(Math.abs(v)) { i = (i + v / Math.abs(v)).mod(size).also { swap(this, i, it) } }
    }
    val i0 = indexOfFirst { it.value == 0L }
    (i0..i0+3000 step 1000).sumOf { this[it%size].value * decryptKey }.run(::println)
}

fun main() {
    generateSequence(::readlnOrNull).map { it.toLong() }.withIndex().toList()
        .also { it.toMutableList().simulate(1) }
        .also { it.toMutableList().simulate(10, 811589153L) }
}
