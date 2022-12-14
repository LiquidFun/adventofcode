fun main() {
    val lines = generateSequence(::readlnOrNull).toList()
        .map { it.split(" -> ", ",").map { it.toInt() }.chunked(2) }
    val width = lines.flatten().maxOf { it[0] } + 200
    val height = lines.flatten().maxOf { it[1] } + 2
    val field = MutableList(height) { MutableList(width) { '.' } }
    fun range(a: Int, b: Int) = minOf(a, b)..maxOf(a, b)
    fun drawLine(rx: IntRange, ry: IntRange) = rx.map { x -> ry.map { y -> field[y][x] = '#' } }
    lines.map { it.zipWithNext { (x1, y1), (x2, y2) -> drawLine(range(x1, x2), range(y1, y2))} }

    fun fill(): Int {
        var endDfs = false
        fun dfs(x: Int, y: Int): Boolean { 
            endDfs = endDfs || y >= field.size || field[0][500] == 'O'
            if (endDfs || field[y][x] != '.')
                return endDfs
            if (!(dfs(x, y+1) || dfs(x-1, y+1) || dfs(x+1, y+1))) 
                field[y][x] = 'O'
            return true
        }
        while (!endDfs) dfs(500, 0)
        return field.flatten().count { it == 'O' } 
    }
    println(fill())
    field.add(MutableList(width) { '#' })
    println(fill())
}
