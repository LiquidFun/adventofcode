// This solution was not golfed whatsoever, it still prints both parts, 
// but is certainly not general to solve any input. However, some of the complexity arises
// a basic because of an ASCII visualization which has been added. 
//
// Set this to true in order to paint a colorful ASCII image (needs ANSI support)
val visualize = false

// This solution only works for inputs of shape:
//
//  ##          #          ##           # 
//  #     or    ##    or    #     or   ##   
// ##           #           ##          #    
//  #          ##           #           ##
//
// Important is: 
//      * it has to be higher than its width 
//      * the middle column must be filled
//      * the remaining 2 blocks have to be on opposite sites, one offset to the other by y=2 blocks

val dirs = listOf(0 to 1, 1 to 0, 0 to -1, -1 to 0)

class Painter(field: List<String>) {
    val visField = field.map { it.toMutableList() }

    var time = 0
    val coords: MutableList<Pair<Int, Int>> = mutableListOf()
    val atTime: MutableMap<Pair<Int, Int>, Int> = mutableMapOf()
    val MAX_TRAIL_LENGTH = 500

    fun add(y: Int, x: Int, c: Char) { 
        visField[y][x] = c
        atTime[y to x] = time
        coords.add(y to x)
        if (coords.size > MAX_TRAIL_LENGTH)
            coords.removeAt(0)
    }

    fun paint(withBackground: Boolean = false) {
        if (!visualize) 
            return
        print("[H")
        var c = 
            if (withBackground) 
                visField[0].indices.flatMap { visField.indices.map { y -> y to it } } 
            else
                coords
        for ((y, x) in c) {
            if (!withBackground && (y to x) !in atTime)
                continue
            fun t(mult: Double = 1.0, atLeast: Int = 50, max: Int = 255): Int = 
                maxOf(atLeast, (max - (time - atTime[y to x]!!) * mult).toInt())
            when (visField[y][x]) {
                '#' -> "[38;2;105;15;0m"
                '.' -> "[38;2;120;120;130m"
                ' ' -> "[38;2;10;20;10m"
                else -> "[38;2;${t(1.0)};${t(0.25)};${t(0.01)}m"
            }.run(::print)
            print("[${x};${y}H▓")
        }
        println()
        time++
    }
}


fun solve(asCube: Boolean, field: List<String>, seq: List<String>) {
    val painter = Painter(field)
    val instructions = Regex("(\\d+|[RL])").findAll(seq[0]).toList()
    var currDir = 0
    var (cy, cx) = 0 to field[0].indexOfFirst { it == '.' }
    painter.paint(true)
    for (instruction in instructions.map { it.value }) {
        if (instruction in "RL") {
            currDir = (currDir + if (instruction == "R") 1 else -1).mod(4)
            continue
        }
        var (ny, nx) = cy to cx
        for (i in 1..instruction.toInt()) {
            painter.paint()
            var ny3 = ny + dirs[currDir].first
            var nx3 = nx + dirs[currDir].second
            var dir3 = currDir

            val yIsShorter = field.size < field[0].length
            val alongShortAxis = (dirs[currDir].first != 0 && yIsShorter) || (dirs[currDir].second != 0 && !yIsShorter)
            if (asCube && (ny3 !in field.indices || nx3 !in field[0].indices)) {
                if (!yIsShorter && alongShortAxis) {
                    dir3 = (dir3 + 2).mod(4)
                    ny3 = (50*2 + ny3 - ny3 % 50 + (49 - ny3 % 50)).mod(field.size)
                    nx3 = nx3 + dirs[dir3].second
                    assert(ny3 in field.indices && nx3 in field[0].indices) { "$ny3 $nx3 out of bounds" }
                }
            }
            ny3 = ny3.mod(field.size)
            nx3 = nx3.mod(field[0].length)
            ny = (ny + dirs[currDir].first).mod(field.size)
            nx = (nx + dirs[currDir].second).mod(field[cy].length)
            var ny2 = ny
            var nx2 = nx
            if (field[ny][nx] == ' ' && field[ny2][nx2] == ' ') {
                var nyxp: MutableList<Pair<Int, Int>> = mutableListOf()
                var nyx2p: MutableList<Pair<Int, Int>> = mutableListOf()
                var nyx3p: MutableList<Pair<Int, Int>> = mutableListOf()
                painter.add(ny3, nx3, '?')
                val moveStraight = !asCube || alongShortAxis && (cy in 0..49 || cy in 100..149)
                while (field[ny][nx] == ' ' && field[ny2][nx2] == ' ') {
                    // If there is an adjacent block go diagonally
                    if (!moveStraight) {
                        ny = (ny + dirs[(currDir+1).mod(4)].first).mod(field.size)
                        nx = (nx + dirs[(currDir+1).mod(4)].second).mod(field[cy].length)
                        ny2 = (ny2 + dirs[(currDir-1).mod(4)].first).mod(field.size)
                        nx2 = (nx2 + dirs[(currDir-1).mod(4)].second).mod(field[cy].length)
                    }

                    if (field[ny][nx] != ' ' || field[ny2][nx2] != ' ' || field[ny3][nx3] != ' ')
                        break
                    if (moveStraight) {
                        ny3 = ny3 + dirs[dir3].first
                        nx3 = nx3 + dirs[dir3].second
                    }
                    else {
                        ny = (ny + dirs[currDir].first).mod(field.size)
                        nx = (nx + dirs[currDir].second).mod(field[cy].length)
                        ny2 = (ny2 + dirs[currDir].first).mod(field.size)
                        nx2 = (nx2 + dirs[currDir].second).mod(field[cy].length)
                    }

                    if (asCube && (ny3 !in field.indices || nx3 !in field[0].indices)) {
                        if (!yIsShorter && alongShortAxis) {
                            dir3 = (dir3 + 2).mod(4)
                            ny3 = (100 + ny3 - ny3 % 50 + (49 - ny3 % 50)).mod(field.size)
                            nx3 = nx3 + dirs[dir3].second
                            assert(ny3 in field.indices && nx3 in field[0].indices) { "$ny3 $nx3 out of bounds" }
                        }
                    }
                    ny3 = ny3.mod(field.size)
                    nx3 = nx3.mod(field[0].length)
                    nyxp.add(ny to nx)
                    nyx2p.add(ny2 to nx2)
                    nyx3p.add(ny3 to nx3)
                }
                if (field[ny][nx] != ' ') {
                    if (field[ny][nx] != '#') 
                        currDir = (currDir+1).mod(4)
                }
                else if (field[ny2][nx2] != ' ') {
                    ny = ny2
                    nx = nx2
                    nyxp = nyx2p
                    if (field[ny][nx] != '#') 
                        currDir = (currDir-1).mod(4)
                }
                else if (field[ny3][nx3] != ' ') {
                    ny = ny3
                    nx = nx3
                    nyxp = nyx3p
                    if (asCube && field[ny][nx] != '#') 
                        currDir = (currDir+2).mod(4)
                }
                for ((nyp, nxp) in nyxp) {
                    painter.add(nyp, nxp, if (currDir % 2 == 0) '\\' else '/')
                    painter.paint()
                }
            }
            if (field[ny][nx] == '.') {
                cy = ny
                cx = nx
                painter.add(cy, cx, ">v<^"[currDir])
            }
            else if (field[ny][nx] == '#')
                break
        }
    }
    painter.paint()
    println(1000 * (cy+1) + 4 * (cx+1) + currDir)
}



fun main() {
    var (field, seq) = generateSequence(::readlnOrNull).joinToString("\n").split("\n\n").map { it.split("\n") }

    // Part 1
    solve(asCube=false, field, seq)

    // Part 2
    val cube = field.map { it.toMutableList() }
    // Rotate last face of cube in input to make it easier
    for (y in 0..49) {
        for (x in 0..49) {
            cube[199-x][50+y] = cube[150+y][x]
            cube[150+y][x] = ' '
        }
    }
    field = cube.map { it.joinToString("") }
    solve(asCube=true, field, seq)
}
