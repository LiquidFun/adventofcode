class Monkey(monkey: String) {
    var counter = 0L
    var items: MutableList<Long>
    var op: (Long) -> Long
    val divisibleBy: Long
    val idIfTrue: Int
    val idIfFalse: Int

    companion object {
        var modulo: Long = 1
        var monkeys: MutableList<Monkey> = mutableListOf()
    }

    init {
        val attributes = monkey.split("\n").map { it.split(":")[1].trim() }
        val (_, _, _, opMultOrAdd, opArg) = attributes[2].split(" ")
        val opFunc: (Long, Long) -> Long = if (opMultOrAdd == "*") Long::times else Long::plus

        items = attributes[1].split(",").map { it.trim().toLong() }.toMutableList()
        op = { x -> opFunc(x, opArg.toLongOrNull() ?: x) }
        divisibleBy = attributes[3].split(" ").last().toLong()
        idIfTrue = attributes[4].split(" ").last().toInt()
        idIfFalse = attributes[5].split(" ").last().toInt()
        Monkey.modulo *= divisibleBy
        Monkey.monkeys.add(this)
    }
    fun round(divideBy: Int = 1) {
        for (item in items) {
            val newWorry = op(item) % Monkey.modulo / divideBy
            val index = if (newWorry % divisibleBy == 0L) idIfTrue else idIfFalse
            Monkey.monkeys[index].items.add(newWorry)
            counter++
        }
        items.clear()
    }
}

fun main() {
    val monkeys = generateSequence(::readlnOrNull).joinToString("\n").trim().split("\n\n")

    fun multLast2() = Monkey.monkeys.map { it.counter }.sorted().takeLast(2).reduce(Long::times)
    fun rounds(count: Int, divBy: Int) = repeat(count) { Monkey.monkeys.map { it.round(divBy) } }

    // Part 1
    monkeys.map { Monkey(it) }
    rounds(20, divBy=3)
    println(multLast2())

    // Part 2
    Monkey.modulo = 1
    Monkey.monkeys.clear()
    monkeys.map { Monkey(it) }
    rounds(10000, divBy=1)
    println(multLast2())
}
