

fun main() {
    val s = generateSequence(::readlnOrNull).toList()
    val indices = (0..s.size-1).toList()
    val visible: MutableSet<Pair<Int, Int>> = mutableSetOf()
    var highest: Int
    for (i in indices) {
        for (order in listOf(indices, indices.reversed())) {
            highest = 0
            for (x in order) {
                if (highest < s[i][x].code)
                    visible.add(Pair(i, x))
                highest = maxOf(s[i][x].code, highest)
            }
            highest = 0
            for (y in order) {
                if (highest < s[y][i].code)
                    visible.add(Pair(y, i))
                highest = maxOf(s[y][i].code, highest)
            }
        }
    }
    println(visible.size)

    var best = 0
    fun is_valid(y: Int, x: Int, size: Int) = 0 <= y && y < size && 0 <= x && x < size
    for (Y in indices) {
        for (X in indices) {
            var scenic = 1
            for ((ya, xa) in listOf(Pair(1, 0), Pair(-1, 0), Pair(0, 1), Pair(0, -1))) {
                var dist = 0
                var y = Y+ya
                var x = X+xa
                while (is_valid(y, x, s.size)) {
                    dist += 1
                    if (s[y][x] >= s[Y][X])
                        break
                    y = y+ya
                    x = x+xa
                }
                scenic *= dist
            }
            best = maxOf(best, scenic)
        }
    }
    println(best)
}
