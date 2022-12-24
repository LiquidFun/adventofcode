typealias Point = Pair<Int, Int>

val dirs = listOf(0 to 1, 1 to 0, 0 to -1, -1 to 0)
val dirsChars: Map<Char, Point> = mapOf('>' to dirs[0], 'v' to dirs[1], '<' to dirs[2], '^' to dirs[3])
fun lcmOf(a: Int, b: Int) = (1..100000).first { it % a == 0 && it % b == 0 }

fun main() {
    val input = generateSequence(::readlnOrNull).toList()
    val (height, width) = (input.size - 2) to (input[0].length - 2)
    val lcm = lcmOf(height, width)
    val blizzards = List<MutableSet<Point>>(lcm+1) { mutableSetOf() }
    for ((y, row) in input.withIndex()) {
        for ((x, v) in row.withIndex()) {
            if (v in dirsChars)
                for (t in 0..lcm)
                    blizzards[t].add(
                            (y + dirsChars[v]!!.first * t - 1).mod(height)+1 to 
                            (x + dirsChars[v]!!.second * t - 1).mod(width)+1
                    )
        }
    }
    // Blizzard repeats every 700 steps
    assert(blizzards[0] == blizzards[lcm])
    assert(blizzards[1] != blizzards[lcm])

    fun isInside(p: Point): Boolean = p.first in input.indices && p.second in input[0].indices

    fun minTimeToMoveFromTo(atTime: Int, from: Point, to: Point): Int {
        val queue = ArrayDeque<Pair<Int, Point>>() 
        queue.add(atTime to from)
        val visited: MutableSet<Pair<Int, Point>> = mutableSetOf()

        while (queue.isNotEmpty()) {
            val (t, yx) = queue.removeFirst()
            val (y, x) = yx
            if (y == to.first && x == to.second)
                return t
            val vis = t % lcm to (y to x)
            if (visited.contains(vis))
                continue
            visited.add(vis)
            for ((ya, xa) in dirs.map { y+it.first to x+it.second }.filter(::isInside)) {
                if (input[ya][xa] != '#' && !blizzards[(t+1).mod(lcm)].contains(ya to xa))
                    queue.add(t+1 to (ya to xa))
            }
            if (!blizzards[(t+1).mod(lcm)].contains(y to x))
                queue.add(t+1 to (y to x))
        }
        return -1
    }
    val start = 0 to 1
    val end = height+1 to width
    val t1 = minTimeToMoveFromTo(0, start, end)
    println(t1)
    val t2 = minTimeToMoveFromTo(t1, end, start)
    val t3 = minTimeToMoveFromTo(t2, start, end)
    println(t3)
}
