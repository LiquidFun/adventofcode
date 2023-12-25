from copy import deepcopy
from itertools import product

s1 = s2 = 0
X, Y, Z = 10, 10, 400
stack = [[[-1] * Z for _ in range(Y)] for _ in range(X)]
bricks = []

for i, line in enumerate(open(0)):
    x1, y1, z1, x2, y2, z2 = map(int, line.replace("~", ",").split(","))
    bricks.append([])
    for x, y, z in product(range(x1, x2+1), range(y1, y2+1), range(z1, z2+1)):
        stack[x][y][z] = i
        bricks[-1].append((x, y, z))

def z_lower(coords):
    return [(x, y, z-1) for x,y,z in coords]

def at_z_lower(coords, stack):
    return {stack[x][y][z-1] for x,y,z in coords}

def at_z_upper(coords, stack):
    return {stack[x][y][z+1] for x,y,z in coords}

def drop_all(stack, bricks):
    changed = True
    dropped = set()
    while changed:
        changed = False
        for z, y, x in product(range(2, Z), range(Y), range(X)):
            if (brick_id := stack[x][y][z]) != -1:
                brick = bricks[brick_id]
                if all(z > 1 for _, _, z in brick):
                    if len(at_z_lower(brick, stack) - {-1, brick_id}) == 0:
                        for x,y,z in brick:
                            stack[x][y][z] = -1
                        brick = bricks[brick_id] = z_lower(brick)
                        for x,y,z in brick:
                            stack[x][y][z] = brick_id
                        dropped.add(brick_id)
                        changed = True
    return dropped

drop_all(stack, bricks)

for i, brick in enumerate(bricks):
    ids_above = at_z_upper(brick, stack) - {-1, i}
    can_remove = True
    for id_above in ids_above:
        supporting_ids = at_z_lower(bricks[id_above], stack) - {-1, id_above}
        if len(supporting_ids) == 1:
            can_remove = False
            stack2 = deepcopy(stack)
            bricks2 = deepcopy(bricks)
            for x,y,z in bricks2[i]:
                stack2[x][y][z] = -1
            bricks2[i] = []
            s2 += len(drop_all(stack2, bricks2) - {i})
            break

    s1 += can_remove

print(s1, s2, sep='\n')
