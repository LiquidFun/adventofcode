fun main() {
    val rucksacks = generateSequence(::readlnOrNull).toList()
    val cost = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    val s1 = rucksacks
        .map { it.chunked(it.length / 2)}
        .map { it[0].toSet() intersect it[1].toSet() }
        .sumOf { cost.indexOf(it.first()) }
    println(s1)

    val s2 = rucksacks
        .chunked(3)
        .map { it[0].toSet() intersect it[1].toSet() intersect it[2].toSet() }
        .sumOf { cost.indexOf(it.first()) }
    println(s2)
}
