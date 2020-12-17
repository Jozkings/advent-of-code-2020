from collections import defaultdict
import itertools

FILE_NAME = "input17.in"


def solve_g(g_map, first_part, cycle):
    new_g_map = defaultdict(str)
    for key, value in g_map.items():
        active = 0
        x, y, z, w = key
        if first_part and w != 0:
            new_g_map[(x, y, z, w)] = g_map[(x, y, z, w)]
            continue
        if z < -cycle or z > cycle:
            new_g_map[(x, y, z, w)] = g_map[(x, y, z, w)]
            continue
        if w < -cycle or w > cycle:
            new_g_map[(x, y, z, w)] = g_map[(x, y, z, w)]
            continue
        for cx, cy, cz, cw in changes:
            if (x+cx, y+cy, z+cz, w + cw) not in g_map:
                continue
            if cx == 0 and cy == 0 and cz == 0 and cw == 0:
                new_g_map[(x, y, z, w)] = g_map[(x, y, z, w)]
                continue
            neigh = g_map[(x+cx, y+cy, z+cz, w + cw)]
            if neigh == "#":
                active += 1
            if active > 3:
                break
        if value == "#":
            if active != 2 and active != 3:
                new_g_map[key] = "."
            else:
                new_g_map[key] = "#"
        elif value == ".":
            if active == 3:
                new_g_map[key] = "#"
            else:
                new_g_map[key] = "."
    return new_g_map


def active_number(map_):
    active = 0
    for key, value in map_.items():
        if value == "#":
            active += 1
    return active


g = []
g_map = defaultdict(str)
CYCLES_NUMBER = 6

for line in open(FILE_NAME).readlines():
    line = line.strip()
    small_g = []
    for character in line:
        small_g.append(character)
    g.append(small_g)

for i in range(-CYCLES_NUMBER, len(g)+CYCLES_NUMBER+1):
    for j in range(-CYCLES_NUMBER, len(g[0])+CYCLES_NUMBER+1):
        for z in range(-CYCLES_NUMBER, CYCLES_NUMBER+1):
            for w in range(-CYCLES_NUMBER, CYCLES_NUMBER+1):
                if z == 0 and w == 0 and 0 <= i < len(g) and 0 <= j < len(g[0]):
                    try:
                        g_map[(i, j, 0, 0)] = g[i][j]
                    except:
                        g_map[(i, j, 0, 0)] = "."
                else:
                    g_map[(i, j, z, w)] = "."


changes = list(itertools.product([-1, 0, 1], repeat=3))
changes = [val + (0, ) for val in changes]
cycles = 0
while cycles != CYCLES_NUMBER:
    if cycles == 0:
        saved_g_map = g_map
    cycles += 1
    g_map = solve_g(g_map, True, cycles)

print(active_number(g_map))

changes = list(itertools.product([-1, 0, 1], repeat=4))
cycles = 0
g_map = saved_g_map
while cycles != CYCLES_NUMBER:
    cycles += 1
    g_map = solve_g(g_map, False, cycles)

print(active_number(g_map))

