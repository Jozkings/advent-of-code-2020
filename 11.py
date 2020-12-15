from copy import deepcopy

FILE_NAME = "input11.in"

g = []
for line in open(FILE_NAME).readlines():
    line = line.strip()
    arr = []
    for char in line:
        arr.append(char)
    g.append(line)

changes = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def apply_change_one(g, i, j, change):
    x, y = change
    new_i, new_j = i + x, y + j
    if new_i < 0 or new_j < 0 or new_i >= len(g) or new_j >= len(g[new_i]):
        return 0
    seat = g[new_i][new_j]
    return seat == "#"


def apply_change_two(g, i, j, change):
    x, y = change
    new_i, new_j = i + x, y + j
    if new_i < 0 or new_j < 0 or new_i >= len(g) or new_j >= len(g[new_i]):
        return 0
    while 0 <= new_i < len(g) and 0 <= new_j < len(g[new_i]):
        seat = g[new_i][new_j]
        if seat == "L":
            return 0
        if seat == "#":
            return 1
        new_i += x
        new_j += y
    return 0


def occupied_number(g):
    occupied = 0
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == "#":
                occupied += 1
    return occupied


def step(g, first_part):
    changed = True
    new_g = deepcopy(g)
    while changed:
        changed = False
        for i in range(len(g)):
            for j in range(len(g[i])):
                occupied = 0
                for change in changes:
                    if first_part:
                        occupied += apply_change_one(g, i, j,  change)
                    else:
                        occupied += apply_change_two(g, i, j, change)
                if occupied == 0 and g[i][j] == "L":
                    new_g[i] = new_g[i][:j] + "#" + new_g[i][j+1:]
                    changed = True
                elif occupied >= 4 and first_part and g[i][j] == "#":
                    new_g[i] = new_g[i][:j] + "L" + new_g[i][j+1:]
                    changed = True
                elif occupied >= 5 and not first_part and g[i][j] == "#":
                    new_g[i] = new_g[i][:j] + "L" + new_g[i][j+1:]
                    changed = True
        g = deepcopy(new_g)
        if not changed:
            return occupied_number(g)


print(step(g, True))
print(step(g, False))
