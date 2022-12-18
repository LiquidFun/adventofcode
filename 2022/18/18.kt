data class Point(var x: Int, var y: Int, var z: Int) {
	operator fun plus(o: Point): Point = Point(x+o.x, y+o.y, z+o.z)
	fun adjacent(): List<Point> = dirs.map { this+it }.toList()
	fun min(): Int = minOf(x, y, z)
	fun max(): Int = maxOf(x, y, z)
}

val dirs = listOf(
	Point(1, 0, 0), Point(0, 1, 0), Point(0, 0, 1),
	Point(-1, 0, 0), Point(0, -1, 0), Point(0, 0, -1),
)

fun main() {
	val input = generateSequence(::readlnOrNull)
		.map { it.split(",").map { it.toInt() } }
		.map { (x, y, z) -> Point(x, y, z) }.toList()
	val bounds = input.minOf { it.min()-1 }..input.maxOf { it.max()+1 }
	
	// Part 1
	input.sumOf { it.adjacent().count { !input.contains(it) } }.run(::println)

	// Part 2
	val queue = mutableListOf(Point(bounds.first, bounds.first, bounds.first))
	val visited: MutableSet<Point> = mutableSetOf()
	var count = 0

	while (queue.isNotEmpty()) {
		val point = queue.removeAt(0)
		if (point in visited) continue
		visited.add(point)
		for (adj in point.adjacent()) {
			if (adj in input) 
				count++
			else if (adj.x in bounds && adj.y in bounds && adj.z in bounds)
				queue.add(adj)
		}
	}
	println(count)
}
