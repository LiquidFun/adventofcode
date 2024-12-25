occ = {".": [], "#": []}

for schematic in open(0).read().split("\n\n"):
    counts = tuple(c.count("#") for c in zip(*schematic.split()))
    occ[schematic[0]].append(counts)

print(sum(all(k+l<=7 for k,l in zip(key,lock)) 
          for key in occ['.'] 
          for lock in occ["#"]))
