val points = mapOf("A Y" to 6, "B Z" to 6, "C X" to 6, "A X" to 3, "B Y" to 3, "C Z" to 3)

fun getPoints(s: String): Int = points.getOrDefault(s, 0) + "-XYZ".indexOf(s[2])

fun List<String>.score() = this.map(::getPoints).sum() 

fun rotate(s: String): Char = "XYZ"[("ABC".indexOf(s[0]) + "YZX".indexOf(s[2])) % 3]

fun List<String>.newStrategy() = this.map { "${it[0]} ${rotate(it)}" }

fun main() {
    val moves = generateSequence(::readlnOrNull).toList()
    println(moves.score())
    println(moves.newStrategy().score())
}
