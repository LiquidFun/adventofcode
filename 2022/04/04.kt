fun Boolean.toInt() = if (this) 1 else 0

fun main() {
    val seq = generateSequence(::readlnOrNull).toList()
        .map { it.replace(',', '-').split('-') }
        .map { it.map { it.toInt() } }
    val s1 = seq
        .map { (a, b, c, d) -> (a..b intersect c..d).size-1 in setOf(b-a, d-c) }
        .sumOf { it.toInt() }
    val s2 = seq
        .map { it[0]..it[1] intersect it[2]..it[3] }
        .sumOf { (!it.isEmpty()).toInt() }
    println(s1)
    println(s2)
}
