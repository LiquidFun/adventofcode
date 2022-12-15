fun dist(x1: Long, y1: Long, x2: Long, y2: Long) = Math.abs(x1 - x2) + Math.abs(y1 - y2)

fun main() {
    val sensors = generateSequence(::readlnOrNull).toList()
        .map { Regex("-?\\d+").findAll(it).toList() }
        .map { it.map { it.value.toLong() } }
        .sortedBy() { it[0] }
    val y = 2_000_000L
    (-1_000_000L..6_000_000L).count { x -> 
        sensors
            .filter { it[2] != x || it[3] != y }
            .any { (xs, ys, xb, yb) -> dist(xs, ys, x, y) <= dist(xs, ys, xb, yb) }
    }.run(::println)

    for (y in 0L..4_000_000L) {
        var x = 0L
        for ((xs, ys, xb, yb) in sensors)
            if (dist(xs, ys, x, y) <= dist(xs, ys, xb, yb))
                x = xs + dist(xs, ys, xb, yb) - Math.abs(ys - y) + 1
        if (x <= 4_000_000L)
            println(x * 4_000_000L + y)
    }
}
