import java.util.PriorityQueue

data class Blueprint(
    val id: Int,
    val oreForOreRobot: Int,
    val oreForClayRobot: Int,
    val oreForObsidianRobot: Int,
    val clayForObsidianRobot: Int,
    val oreForGeodeRobot: Int,
    val obsidianForGeodeRobot: Int,
)

data class State(
    var timeLeft: Int,
    var ore: Int = 0,
    var clay: Int = 0,
    var obsidian: Int = 0,
    var geode: Int = 0,
    var oreRobots: Int = 1,
    var clayRobots: Int = 0,
    var obsidianRobots: Int = 0,
    var geodeRobots: Int = 0,
) : Comparable<State> {

    fun handleMinute(): State { 
        timeLeft--; 
        ore += oreRobots; clay += clayRobots; obsidian += obsidianRobots; geode += geodeRobots; 
        return this 
    }

    override fun compareTo(other: State) = compareValuesBy(this, other, { it.heuristicScore() })

    fun heuristicScore() = oreRobots + clayRobots + obsidianRobots + geodeRobots

    fun isBetterThan(other: State): Boolean = ore >= other.ore
        && clay >= other.clay
        && obsidian >= other.obsidian
        && geode >= other.geode
        && oreRobots >= other.oreRobots
        && clayRobots >= other.clayRobots
        && obsidianRobots >= other.obsidianRobots
        && geodeRobots >= other.geodeRobots
}

fun maxGeodes(blueprint: Blueprint, initialTimeLeft: Int): Int {
    val queue = ArrayDeque<State>()
    queue.add(State(initialTimeLeft))

    val bestRobots = PriorityQueue<State>()
    val visited: MutableSet<State> = mutableSetOf()

    fun addState(state: State) {
        if (state in visited)
            return
        visited.add(state)
        for (robot in bestRobots) {
            if (robot.isBetterThan(state))
                return
        }
        bestRobots.add(state)
        if (bestRobots.size > 1000)
            bestRobots.poll()
        queue.add(state)
    }

    var best = 0
    while (queue.isNotEmpty()) {
        val state = queue.removeFirst()
        val minute = state.copy().handleMinute()
        if (minute.timeLeft == 0) {
            best = maxOf(best, minute.geode)
            continue
        }
        if (state.ore >= blueprint.oreForGeodeRobot && state.obsidian >= blueprint.obsidianForGeodeRobot)
            minute.copy(
                ore=minute.ore-blueprint.oreForGeodeRobot,
                obsidian=minute.obsidian-blueprint.obsidianForGeodeRobot,
                geodeRobots=minute.geodeRobots + 1
            ).run(::addState)
        else if (state.ore >= blueprint.oreForObsidianRobot && state.clay >= blueprint.clayForObsidianRobot)
            minute.copy(
                ore=minute.ore-blueprint.oreForObsidianRobot,
                clay=minute.clay-blueprint.clayForObsidianRobot,
                obsidianRobots=minute.obsidianRobots + 1
            ).run(::addState)
        else {
            if (state.ore >= blueprint.oreForClayRobot) {
                minute.copy(ore=minute.ore-blueprint.oreForClayRobot, clayRobots=minute.clayRobots + 1).run(::addState)
            }
            if (state.ore >= blueprint.oreForOreRobot) {
                minute.copy(ore=minute.ore-blueprint.oreForOreRobot, oreRobots=minute.oreRobots+1).run(::addState)
            }
            addState(minute.copy())
        }
    }
    return best
}

fun main() {
    val input = generateSequence(::readlnOrNull).toList()
        .map { Regex("\\d+").findAll(it).map { it.value.toInt() }.toList() }
        .map { Blueprint(it[0], it[1], it[2], it[3], it[4], it[5], it[6]) }

    println(input.map { maxGeodes(it, 24) }.zip(input) { geodes, blueprint -> geodes * blueprint.id }.sum())
    println(input.slice(0..2).map { maxGeodes(it, 32) }.reduce { s, e -> s * e })
}
