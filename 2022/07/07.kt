data class Tree(val name: String, var parent: Tree?) {
    var size: Int = 0
    val children: MutableList<Tree> = mutableListOf()
}

fun main() {
    val shell = generateSequence(::readlnOrNull).toList()
        .map { it.replace("$ ", "") }
        .filter { it != "ls" }
    val root = Tree("/", null)
    var current = root
    for (line in shell) {
        var (command, arg) = line.split(" ")
        when (command) {
            "cd" -> when (arg) {
                "/" -> current = root
                ".." -> current = current.parent!!
                else -> current = current.children.filter { it.name == arg }.first()
            }
            "dir" -> current.children.add(Tree(arg, current))
            else -> current.size += command.toInt()
        }
    }
    val sizes: MutableList<Int> = mutableListOf()
    fun recursiveSizes(tree: Tree): Int {
        sizes.add(tree.size + tree.children.sumOf(::recursiveSizes) )
        return sizes.last()
    }
    recursiveSizes(root)
    println(sizes.filter { it <= 100000 }.sum())
    val needed = 30000000 - (70000000 - sizes.max())
    println(sizes.filter { it >= needed }.min())
}
