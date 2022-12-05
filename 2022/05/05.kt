fun solve(input: String, moveTogether: Boolean) {
    val (raw_towers, moves) = input.split("\n\n")
    val towers = raw_towers.split("\n").dropLast(1).asReversed()
    val stacks: MutableList<MutableList<Char>> = mutableListOf()

    for (j in 1 until towers[0].length step 4) {
        stacks.add(mutableListOf())
        for (i in 0 until towers.size)
            if (towers[i][j] != ' ')
                stacks.last().add(towers[i][j])
    }
    val nums = moves
        .split("\n")
        .map {it.filter {!it.isLetter()}}
        .map { it.split("  ")}
        .map { it.map {it.trim().toInt()}}

    for ((num, from, to) in nums) {
        if (!moveTogether) 
            for (i in 1..num)
                stacks[to-1].add(stacks[from-1].removeLast())
        else {
            val tmp: MutableList<Char> = mutableListOf()
            for (i in 1..num)
                tmp.add(stacks[from-1].removeLast())
            for (i in 1..num)
                stacks[to-1].add(tmp.removeLast())

        }
    }
    println(stacks.map { it.last() }.joinToString(""))
}

fun main() {
    val input = generateSequence(::readlnOrNull).joinToString("\n")
    solve(input, false)
    solve(input, true)
}
