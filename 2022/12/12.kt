fun bfs(field: List<String>, queue: MutableList<Pair<Int, Int>>, target: Pair<Int, Int>): Int {
    val dist: MutableMap<Pair<Int, Int>, Int> = mutableMapOf()
    queue.forEach { dist[it] = 0 }
    val dirs = listOf(-1 to 0, 1 to 0, 0 to 1, 0 to -1)
    fun isValid(y: Int, x: Int) = 0 <= y && y < field.size && 0 <= x && x < field[0].length
    while (!queue.isEmpty()) {
        val (y, x) = queue.removeFirst()
        dirs
            .map { (ya, xa) -> Pair(y+ya, x+xa) }
            .filter { isValid(it.first, it.second) }
            .filter { !dist.contains(it) }
            .filter { (ya, xa) -> field[y][x] + 1 >= field[ya][xa] }
            .forEach { 
                dist[it] = dist[Pair(y, x)]!! + 1
                queue.add(it)
            }
    }
    return dist[target]!!
}

fun main() {
    var field = generateSequence(::readlnOrNull).toList()
    fun findChars(c: Char) = field
        .mapIndexed { y, l -> l.mapIndexed { x, _ -> y to x } }
        .flatten()
        .filter { field[it.first][it.second] == c }
        .toMutableList()
    val S = findChars('S')
    val E = findChars('E').first()
    field = field.map { it.replace("S", "a").replace("E", "z") }
    println(bfs(field, S, E))
    println(bfs(field, findChars('a'), E))
}
