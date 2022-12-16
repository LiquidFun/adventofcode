import java.util.PriorityQueue

data class State(
        var time: Int,
        var current: String,
        var elTime: Int? = null,
        var elephant: String? = null,
        var opened: Set<String> = setOf(),
        var flow: Int = 0,
) : Comparable<State> {
    override fun compareTo(other: State) = compareValuesBy(this, other, { -it.flow })
}

fun main() {
    val input = generateSequence(::readlnOrNull).toList()
        .map { Regex("([A-Z]{2}|\\d+)").findAll(it).toList().map { it.value } }
    val neighbors = input.associate { it[0] to it.slice(2..it.size-1) }
    val flows = input.associate { it[0] to it[1].toInt() }

    fun getNonZeroNeighbors(curr: String, dist: Int = 0, visited: Set<String> = setOf()): Map<String, Int> {
        val neigh = HashMap<String, Int>()
        for (neighbor in neighbors[curr]!!.filter { it !in visited }) {
            if (flows[neighbor]!! != 0)
                neigh[neighbor] = dist+1
            for ((name, d) in getNonZeroNeighbors(neighbor, dist+1, visited + setOf(curr)))
                neigh[name] = minOf(d, neigh.getOrDefault(name, 1000))
        }
        return neigh
    }
    val nonZeroNeighbors = input.associate { it[0] to getNonZeroNeighbors(it[0]) }

    fun solve(initialState: State): Int {
        val queue = PriorityQueue<State>().also { it.add(initialState) }
        var best = 0
        val visited: MutableMap<List<String>, Int> = mutableMapOf()
        while (queue.isNotEmpty()) {
            var (time, current, elTime, elephant, opened, flow) = queue.remove()
            best = maxOf(best, flow)
            val vis = (opened.toList() + listOf(current, elephant ?: "")).sorted()
            if (visited.getOrDefault(vis, -1) >= flow)
                continue
            visited[vis] = flow
            if (elTime != null && elephant != null && time < elTime) {
                time = elTime.also { elTime = time }
                current = elephant.also { elephant = current }
            }
            for ((neighbor, dist) in nonZeroNeighbors[current]!!) {
                val newTime = time-dist-1
                val newFlow = flow+flows[neighbor]!!*newTime
                if (newTime >= 0 && neighbor !in opened)
                    queue.add(State(newTime, neighbor, elTime, elephant, opened+setOf(neighbor), newFlow))
            }
        }
        return best
    }
    solve(State(30, "AA")).run(::println)
    solve(State(26, "AA", 26, "AA")).run(::println)  // Takes ~10 seconds

}
