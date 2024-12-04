X = [l.strip() + "   " for l in open(0).readlines()]
X.extend([" " * len(X[0])] * 3)
s1 = s2 = 0 

for y in range(len(X)-3):
    for x in range(len(X[y])-3):
        s1 += sum(word in ("XMAS", "SAMX") for word in [
            X[y][x] + X[y+1][x+1] + X[y+2][x+2] + X[y+3][x+3],
            X[y][x] + X[y+1][x] + X[y+2][x] + X[y+3][x],
            X[y][x] + X[y][x+1] + X[y][x+2] + X[y][x+3],
            X[y+3][x] + X[y+2][x+1] + X[y+1][x+2] + X[y][x+3],
        ])

        a = (X[y][x] +  X[y+1][x+1] +  X[y+2][x+2]) in ("MAS", "SAM")
        b = (X[y+2][x] +  X[y+1][x+1] +  X[y][x+2]) in ("MAS", "SAM")
        s2 += a and b

print(s1, s2, sep="\n")
