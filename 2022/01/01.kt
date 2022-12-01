fun main() {
    // val elves = []
    val input = generateSequence(::readlnOrNull).toList()
    val groups = input.scan(0) { s, e -> s + if(e == "") 1 else 0 } 
    val elves = input
        .map { it.toIntOrNull() }
        .withIndex()
        .filter { it.value != null }
        .groupBy { groups[it.index] }
        .values
        .map { it.sumOf { it.value!! } }
        .sorted()

    println(elves.last())
    println(elves.takeLast(3).sum())

}
