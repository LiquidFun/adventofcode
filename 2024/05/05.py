rules, pages = open(0).read().split("\n\n")
rules = {tuple(r.split("|")) for r in rules.splitlines()}

s1 = s2 = 0
for row in pages.splitlines():
    n = row.split(",")
    n2 = n[:]
    if all(n.index(b) < n.index(a) for b, a in rules if b in n and a in n):
        s1 += int(n[len(n)//2])
    else:
        new = []
        i = -1
        while n:
            i = (i + 1) % len(n)
            if all(b not in n or b in new for b, a in rules if n[i] == a):
                new.append(n.pop(i))
        s2 += int(new[len(new)//2])
                
print(s1, s2, sep="\n")
