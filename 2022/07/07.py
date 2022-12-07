import sys
from dataclasses import dataclass, field

@dataclass
class Tree:
    name: str
    parent: "Tree" = None
    size: int = 0
    children: dict = field(default_factory=dict)

current = root = Tree("/")

for line in sys.stdin.read().strip().split("\n"):
    match line.split():
        case ["$", "cd", "/"]:
            current = root
        case ["$", "cd", ".."]:
            current = current.parent or current
        case ["$", "cd", name]:
            current = current.children[name]
        case ["$", "ls"]:
            pass
        case ["dir", name]:
            current.children[name] = Tree(name, current)
        case [num, name]:
            current.size += int(num)

sizes = []
def rec_size(tree):
    size = (tree.size or 0) + sum(map(rec_size, tree.children.values()))
    sizes.append(size)
    return size

rec_size(root)

print(sum(s for s in sizes if s <= 100000))
needed = 30000000 - (70000000 - max(sizes))
print(min([a for a in sorted(sizes) if a >= needed]))


