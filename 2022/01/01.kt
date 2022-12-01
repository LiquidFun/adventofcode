fun main() {
    val input = generateSequence(::readlnOrNull).toList()
    val groups = input.scan(0) { s, e -> s + if (e == "") 1 else 0 } 
    val elves = input
        .map { it.toIntOrNull() }
        .withIndex()
        .filter { it.value != null }
        .groupBy { groups[it.index] }
        .map { it.value.sumOf { it.value!! } }

    println(elves.max())
    println(elves.sorted().takeLast(3).sum())
}
