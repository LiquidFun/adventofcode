fun bfs(field: List<String>, queue: MutableList<Pair<Int, Int>>, target: Pair<Int, Int>): Int {
    val dist = queue.associate { it to 0 }.toMutableMap()
    val dirs = listOf(-1 to 0, 1 to 0, 0 to 1, 0 to -1)
    while (!queue.isEmpty()) {
        val (y, x) = queue.removeFirst()
        dirs
            .map { (ya, xa) -> Pair(y+ya, x+xa) }
            .filter { (ya, xa) -> ya in field.indices && xa in field[0].indices }
            .filter { !dist.contains(it) }
            .filter { (ya, xa) -> field[ya][xa] <= field[y][x] + 1 }
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
        .filter { (y, x) -> field[y][x] == c }
        .toMutableList()
    val S = findChars('S')
    val E = findChars('E').first()
    field = field.map { it.replace("S", "a").replace("E", "z") }
    println(bfs(field, S, E))
    println(bfs(field, findChars('a'), E))
}
