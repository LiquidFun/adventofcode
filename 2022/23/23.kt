typealias Point = Pair<Int, Int> 

val DIRS8 = listOf(-1 to -1, -1 to 0, -1 to 1, 0 to 1, 1 to 1, 1 to 0, 1 to -1, 0 to -1)
val DIRS = mutableListOf(
        listOf(DIRS8[0], DIRS8[1], DIRS8[2]), // N
        listOf(DIRS8[4], DIRS8[5], DIRS8[6]), // S
        listOf(DIRS8[6], DIRS8[7], DIRS8[0]), // E
        listOf(DIRS8[2], DIRS8[3], DIRS8[4]), // W
)

fun main() {
    val input = generateSequence(::readlnOrNull)
        .flatMapIndexed { y, row -> row.mapIndexed { x, v -> (y to x) to v } }
        .filter { it.second == '#' }
        .map { it.first }
        .toMutableSet()
    var round = 0
    while (true) {
        val proposals: MutableMap<Point, MutableList<Point>> = mutableMapOf()
        for ((y, x) in input) {
            val adj = DIRS.map { it.map { (ya, xa) -> y+ya to x+xa } }
            if (adj.flatten().count { input.contains(it) } > 0)
                for (dirs in adj) {
                    if (dirs.count { input.contains(it) } > 0)
                        continue
                    if (dirs[1] !in proposals)
                        proposals[dirs[1]] = mutableListOf()
                    proposals[dirs[1]]!!.add(y to x)
                    break
                }
        }
        for ((point, candidates) in proposals) {
            if (candidates.size == 1) {
                input.remove(candidates[0])
                input.add(point)
            }
        }
        DIRS.add(DIRS.removeAt(0))
        round++
        if (round == 10) {
            val minY = input.minOf { it.first }
            val minX = input.minOf { it.second }
            val maxY = input.maxOf { it.first }
            val maxX = input.maxOf { it.second }
            println((maxY - minY + 1) * (maxX - minX + 1) - input.size)
        }
        if (proposals.isEmpty())
            break
    }
    println(round)
}
