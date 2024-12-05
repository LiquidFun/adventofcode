rules, pages = open(0).read().split("\n\n")
rules = {tuple(r.split("|")) for r in rules.splitlines()}

s = [0, 0]
for row in pages.splitlines():
    old, new = row.split(","), []
    for o in old * 100:
        if o in new: continue
        if all(b in new for b, a in rules if o == a and b in old):
            new.append(o)
    s[new != old] += int(new[len(new)//2])
 
print(*s, sep="\n")
