data class Point(var x: Int, var y: Int, var z: Int) {
	operator fun plus(o: Point): Point = Point(x+o.x, y+o.y, z+o.z)
	fun adjacent(): List<Point> = dirs.map { this+it }.toList()
}

val dirs = listOf(
	Point(1, 0, 0), Point(0, 1, 0), Point(0, 0, 1),
	Point(-1, 0, 0), Point(0, -1, 0), Point(0, 0, -1),
)

fun main() {
	val input = generateSequence(::readlnOrNull)
		.map { it.split(",").map { it.toInt() } }
		.map { (x, y, z) -> Point(x, y, z) }.toList()
	val limitsX = input.minOf { it.x-1 }..input.maxOf { it.x+1 }
	val limitsY = input.minOf { it.y-1 }..input.maxOf { it.y+1 }
	val limitsZ = input.minOf { it.z-1 }..input.maxOf { it.z+1 }
	
	// Part 1
	input.sumOf { it.adjacent().count { !input.contains(it) } }.run(::println)

	// Part 2
	val queue = ArrayDeque<Point>()
	queue.add(Point(limitsX.first, limitsY.first, limitsZ.first))
	var count = 0
	val visited: MutableSet<Point> = mutableSetOf()
	while (queue.isNotEmpty()) {
		val point = queue.removeFirst()
		if (point in visited) continue
		visited.add(point)
		for (adj in point.adjacent()) {
			if (adj in input) 
				count++
			else if (adj.x in limitsX && adj.y in limitsY && adj.z in limitsZ)
				queue.add(adj)
		}
	}
	println(count)
}
