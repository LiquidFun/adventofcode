fun String.solve(n: Int) = n + this.windowed(n).indexOfFirst { it.toSet().size == it.length }

fun main() {
    val s = readln()
    println(s.solve(4))
    println(s.solve(14))
}
