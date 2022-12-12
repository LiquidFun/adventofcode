
class Monkey(monkey: String, divideBy: Int = 1) {
    companion object {
        var modulo: Long = 1
        var monkeys: MutableList<Monkey> = mutableListOf()
    }
    var counter = 0L
    val divideBy = divideBy
    val attributes = monkey.split("\n").drop(1).map { it.split(":")[1].trim() }

    val items = attributes[0].split(",").map { it.trim().toLong() }.toMutableList()
    val opMultOrAdd = attributes[1].split(" ")[3]
    val opArg = attributes[1].split(" ")[4]
    val opFunc: (Long, Long) -> Long = if (opMultOrAdd == "*") Long::times else Long::plus
    fun op(x: Long) = opFunc(x, if (opArg == "old") x else opArg.toLong())
    val divisibleBy = attributes[2].split(" ").last().toLong()
    val ifTrue = attributes[3].split(" ").last().toInt()
    val ifFalse = attributes[4].split(" ").last().toInt()
    init {
        Monkey.modulo *= divisibleBy
        Monkey.monkeys.add(this)
    }
    fun round() {
        for (item in items) {
            val newWorry = op(item) % Monkey.modulo / divideBy
            val index = if (newWorry % divisibleBy == 0L) ifTrue else ifFalse
            Monkey.monkeys[index].items.add(newWorry)
            counter++
        }
        items.clear()
    }
}

fun main() {
    val monkeys = generateSequence(::readlnOrNull).joinToString("\n").trim().split("\n\n")

    fun multLast2() = Monkey.monkeys.map { it.counter }.sorted().takeLast(2).reduce(Long::times)
    fun rounds(count: Int) = (1..count).map { Monkey.monkeys.map { it.round() } }

    // Part 1
    monkeys.map { Monkey(it, divideBy=3) }
    rounds(20)
    println(multLast2())

    // Part 2
    Monkey.modulo = 1
    Monkey.monkeys.clear()
    monkeys.map { Monkey(it) }
    rounds(10000)
    println(multLast2())
}
