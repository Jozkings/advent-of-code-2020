FILE_NAME = "input12.in"

with open(FILE_NAME, 'r') as file:
    vals = [line.strip() for line in file]


def move_first(coords):
    x, y = coords
    facing = 1   #N, E, S, W
    for value in vals:
        dir, number = value[0], int(value[1:])
        if dir == "N":
            x += number
        elif dir == "S":
            x -= number
        elif dir == "E":
            y += number
        elif dir == "W":
            y -= number
        elif dir == "R":
            facing += number // 90
            facing %= 4
        elif dir == "L":
            facing -= number // 90
            facing %= 4
        elif dir == "F":
            if facing == 2 or facing == 3:
                number *= -1
            if facing % 2 == 0:
                x += number
            else:
                y += number
    return abs(x) + abs(y)


def move_second(coords):
    x, y, waypoint_x, waypoint_y = coords
    for value in vals:
        dir, number = value[0], int(value[1:])
        if dir == "N":
            waypoint_x += number
        elif dir == "S":
            waypoint_x -= number
        elif dir == "E":
            waypoint_y += number
        elif dir == "W":
            waypoint_y -= number
        elif dir == "L":
            how_much = number // 90
            if how_much == 1:
                waypoint_x *= -1
            elif how_much == 2:
                waypoint_x *= -1
                waypoint_y *= -1
            elif how_much == 3:
                waypoint_y *= -1
            if how_much % 2 == 1:
                waypoint_x, waypoint_y = waypoint_y, waypoint_x
        elif dir == "R":
            how_much = number // 90
            if how_much == 1:
                waypoint_y *= -1
            elif how_much == 2:
                waypoint_x *= -1
                waypoint_y *= -1
            elif how_much == 3:
                waypoint_x *= -1
            if how_much % 2 == 1:
                waypoint_x, waypoint_y = waypoint_y, waypoint_x
        elif dir == "F":
            for i in range(number):
                x += waypoint_x
                y += waypoint_y
    return abs(x) + abs(y)


x, y = 0, 0
waypoint_x, waypoint_y = 1, 10
print(move_first([x, y]))
print(move_second([x, y, waypoint_x, waypoint_y]))



