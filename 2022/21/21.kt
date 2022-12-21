fun main() {
    val input = generateSequence(::readlnOrNull).map { it.split(": ") }.toList()
    val known = input
        .filter { (_, value) -> value[0].isDigit() }
        .associate { (name, value) -> name to value.toDouble() }
        .toMutableMap()
    val inputsWithOps = input.filter { " " in it[1] }.map { (n, v) -> n to v.split(" ") }

    fun updateKnown() {
        for (i in 1..50) for ((name, value) in inputsWithOps) {
            var (var1, op, var2) = value
            if (var1 in known && var2 in known)
                known[name] = when (op) {
                    "+" -> known[var1]!! + known[var2]!!
                    "-" -> known[var1]!! - known[var2]!!
                    "*" -> known[var1]!! * known[var2]!!
                    "/" -> known[var1]!! / known[var2]!!
                    else -> 0.0
                }
        }
    }
    updateKnown()
    println(Math.round(known["root"]!!))
    val (rootVar1, _, rootVar2) = inputsWithOps.single { it.first == "root" }.second

    fun binSearch(increasing: Boolean): Long? {
        var (lo, hi) = -1e20 to 1e20
        repeat (100) {
            val mid = (lo + hi) / 2L
            known["humn"] = Math.round(mid).toDouble()
            updateKnown()
            if (known[rootVar1]!! == known[rootVar2]!!)
                return Math.round(mid)
            if ((known[rootVar1]!! > known[rootVar2]!!) xor increasing)
                hi = mid
            else
                lo = mid
        }
        return null
    }
    println(listOf(binSearch(true), binSearch(false)).firstNotNullOf { it })
}
