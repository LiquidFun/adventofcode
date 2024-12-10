def solve1(files, s=0, index=-1, f=-1):
    while f+1 < len(files):
        file = files[f := f + 1]
        is_file = f%2 == 0
        for _ in range(file):
            i = f//2 if is_file else len(files) // 2
            s += i * (index := index + 1)
            if not is_file:
                files[-1] -= 1
                while files[-1] == 0 or len(files) % 2 == 0 and len(files)-1 != f:
                    files.pop()
                if len(files)-1 == f:
                    break
    return s

def solve2(files, free_spaces, s=0, index=-1):
    spaces = [[] for j in free_spaces]
    files = list(enumerate(files))

    for i, file in reversed(files):
        for j, empty in enumerate(free_spaces):
            if i <= j:
                break
            if empty >= file:
                spaces[j].append((i, file))
                files[i] = (0, file)
                free_spaces[j] -= file
                break

    for file, space, empty in zip(files, spaces, free_spaces):
        for i, count in [file] + space + [(0, empty)]:
            while count:
                s += i * (index := index + 1)
                count -= 1
    return s

filesystem = [int(a) for a in input()]
print(solve1(filesystem[:]))
print(solve2(filesystem[::2], filesystem[1::2]))
