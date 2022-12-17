val rocks = "@@@@  .@. @@@ .@.  ..@ ..@ @@@  @ @ @ @  @@ @@".split("  ").map { it.split(" ") }
var input: List<Int> = listOf()

data class Tower(
    var stack: ArrayDeque<MutableList<Char>> = ArrayDeque<MutableList<Char>>(),
    var occ: MutableMap<List<Int>, Int> = mutableMapOf(),
    var highestRockIndex: Int = 0,
    var dirIndex: Int = 0,
    var indicesOfMostCommon: MutableList<Int> = mutableListOf(),
    var mostCommon: List<Int>? = null,
    var towerHeightLastSim: Long = 0L,
    var towerHeight: Long = 0L,
) {
    init {
        stack.addFirst(MutableList<Char>(9) { '-' })
    }
}

fun Tower.simulate(rockCount: Int, multiply: Long = 1L): Tower {
    val towerHeightBefore = stack.count { it.contains('#') }
    for (rockIndex in 0..rockCount-1) {
        val rock = rocks[rockIndex % 5]
        val needed = rock.size + 3 - highestRockIndex
        repeat(needed) {
            stack.addFirst(mutableListOf('|', '.', '.', '.', '.', '.', '.', '.', '|'))
            highestRockIndex++
        }
        var starty = highestRockIndex - 3 - rock.size
        for (y in 0..rock.size-1) {
            for (x in 0..rock[y].length-1) {
                stack[starty+y][x+3] = rock[y][x]
            }
        }

        val cols = MutableList<Int>(7){stack.size-1}
        for (x in 1..7)
            for (y in 0..stack.size-1)
                if (stack[y][x] == '#') {
                    cols[x-1] = y
                    break
                }
        cols.minOrNull()!!.run { (0..6).forEach { cols[it] -= this } }
        cols.add(rockIndex % 5)
        occ[cols] = occ.getOrDefault(cols, 0) + 1
        if (mostCommon != null && cols == mostCommon)
            indicesOfMostCommon.add(rockIndex)

        while (true) {
            val dir = input[dirIndex % input.size]
            dirIndex++

            // Left right (dir)
            var isLegal = true
            val lastx = stack[0].size-2
            val endy = starty + rock.size
            for (y in starty..endy)
                for (x in 1..lastx)
                    if (stack[y][x] == '@')
                        isLegal = isLegal && stack[y][x+dir] in ".@"

            if (isLegal) {
                for (y in starty..endy) {
                    var new = stack[y].joinToString("").replace("@", ".").toMutableList()
                    for (x in 1..lastx) {
                        if (stack[y][x] == '@') {
                            new[x+dir] = '@'
                        }
                    }
                    stack[y] = new
                }
            }

            // Downward
            isLegal = true
            for (y in starty..endy)
                for (x in 1..lastx)
                    if (stack[y][x] == '@')
                        isLegal = isLegal && stack[y+1][x] in ".@"

            if (isLegal) {
                for (y in endy downTo starty+1) {
                    for (x in 1..lastx) {
                        if (stack[y-1][x] == '@') {
                            stack[y][x] = '@'
                            stack[y-1][x] = '.'
                        }
                    }
                }
            } else {
                for (y in starty..endy)
                    stack[y] = stack[y].joinToString("").replace("@", "#").toMutableList()
                while (stack[highestRockIndex-1].contains('#'))
                    highestRockIndex--
                break
            }
            starty++
        }
    }
    towerHeightLastSim = (stack.count { it.contains('#') } - towerHeightBefore) * multiply
    towerHeight += towerHeightLastSim
    return this
}

fun main() {
    input = readln().repeat(2).map { if (it == '>') 1 else -1 }
    Tower().simulate(2022).towerHeight.run(::println)

    val forOcc = Tower().simulate(input.size)
    val mostCommon = forOcc.occ.maxBy { it.value }.key
    val indices = Tower(mostCommon=mostCommon).simulate(input.size).indicesOfMostCommon

    val repeatsAfter = indices.flatMap { a -> indices.map { Math.abs(a - it) } }
        .filter { it != 0 }.groupingBy { it }.eachCount().maxBy { it.value }.key

    val target = 1000000000000L
    val goal = Tower().simulate(1000).simulate(repeatsAfter).towerHeightLastSim
    for (initial in 0..input.size-1 step 5) {
        val part2 = Tower().simulate(initial)
        val mult = (target - initial) / repeatsAfter
        val mod = (target - initial) % repeatsAfter

        if (part2.simulate(repeatsAfter).towerHeightLastSim == goal) {
            part2
                .simulate(repeatsAfter, multiply=mult-1L)
                .simulate(mod.toInt())
                .run { println(this.towerHeight) }
                break
        }
    }
}
