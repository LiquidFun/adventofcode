fun main() {
    val sensors = generateSequence(::readlnOrNull).toList()
        .map { Regex("-?\\d+").findAll(it).toList() }
        .map { it.map { it.value.toLong() } }
        .sortedWith() { a: List<Long>, b: List<Long> -> a[0].compareTo(b[0]) }
    fun dist(x1: Long, y1: Long, x2: Long, y2: Long) = Math.abs(x1 - x2) + Math.abs(y1 - y2)
    val y = 2_000_000L
    (-1_000_000L..6_000_000L).map { x -> 
        sensors
            .filter { (_, _, xb, yb) -> xb != x || yb != y }
            .map { (xs, ys, xb, yb) -> dist(xs, ys, xb, yb) >= dist(xs, ys, x, y) }
            .any { it }
    }.count { it }.run(::println)

    for (y in 0L..4_000_000L) {
        var x = 0L
        for ((xs, ys, xb, yb) in sensors)
            if (dist(xs, ys, xb, yb) >= dist(xs, ys, x, y))
                x = xs + dist(xs, ys, xb, yb) - Math.abs(ys - y) + 1
        if (x <= 4_000_000L)
            println(x * 4_000_000L + y)
    }
}
