from collections import defaultdict

FILE_NAME = "input24.in"

dirs = {"e":(1, 0), "se":(0.5, 0.5), "w":(-1, 0), "nw":(-0.5, -0.5), "ne":(0.5, -0.5), "sw":(-0.5, 0.5)}
positions = []

with open(FILE_NAME, 'r') as file:
    for line in file:
        value = line.strip()
        positions.append(value)


def get_black_count(tiles):
    return sum(value for value in tiles.values() if value == 1)


def get_neighbours(position):
    x, y = position
    return [(x + 1, y), (x + 0.5, y + 0.5), (x - 1, y), (x - 0.5, y - 0.5), (x + 0.5, y - 0.5), (x - 0.5, y + 0.5)]


def add_neighbours(tiles):
    new_tiles = defaultdict(int)
    for position, value in tiles.items():
        neighbours = get_neighbours(position)
        for neigh in neighbours:
            if neigh in tiles:
                new_tiles[neigh] = tiles[neigh]
            else:
                new_tiles[neigh] = 0
        new_tiles[position] = value
    return new_tiles

tiles = defaultdict(int)   #0 -> white tile, 1 -> black tile

for position in positions:   #PART 1
    x, y = 0, 0
    two_dirs = False
    for i in range(len(position)):
        if two_dirs:
            two_dirs = False
        else:
            direction = position[i]
            if position[i] != "e" and position[i] != "w":
                direction += position[i+1]
                two_dirs = True
            change_x, change_y = dirs[direction]
            x += change_x
            y += change_y
    tiles[(x, y)] = (tiles[(x, y)] + 1) % 2


print(get_black_count(tiles))

days = 100
tiles = add_neighbours(tiles)    #PART 2
for day in range(days):
    new_tiles = defaultdict(int)
    for position, value in tiles.items():
        blacks = 0
        neighbours = get_neighbours(position)
        for neighbour in neighbours:
            if neighbour in tiles:
                blacks += (tiles[neighbour] == 1)
        new_tiles[position] = tiles[position]
        if value == 1:
            if blacks == 0 or blacks > 2:
                new_tiles[position] = 0
        else:
            if blacks == 2:
                new_tiles[position] = 1
    tiles = add_neighbours(new_tiles)

print(get_black_count(tiles))