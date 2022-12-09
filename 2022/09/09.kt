operator fun Pair<Int, Int>.plus(o: Pair<Int, Int>) = Pair(this.first + o.first, this.second + o.second)

fun main() {
    val input = generateSequence(::readlnOrNull).toList().map { it.split(" ") }
    val visited2: MutableSet<Pair<Int, Int>> = mutableSetOf()
    val visited10: MutableSet<Pair<Int, Int>> = mutableSetOf()
    val lookup = mapOf("D" to Pair(0, 1), "U" to Pair(0, -1), "L" to Pair(-1, 0), "R" to Pair(1, 0))
    val rope = MutableList(10) { Pair(0, 0) }
    for ((dir, steps) in input) {
        for (j in 1..steps.toInt()) {
            rope[0] = rope[0] + lookup[dir]!!
            for (i in 0..rope.size-2) {
                val dx = rope[i].first - rope[i+1].first
                val dy = rope[i].second - rope[i+1].second
                if (Math.abs(dx) >= 2 || Math.abs(dy) >= 2)
                    rope[i+1] = rope[i+1] + Pair(dx.coerceIn(-1..1), dy.coerceIn(-1..1))
            }
            visited2.add(rope[1])
            visited10.add(rope.last())
        }
    }
    println(visited2.size)
    println(visited10.size)
}
