FILE_NAME = "input3.in"

with open(FILE_NAME, 'r') as file:
    G = [line.strip() for line in file]

index = 0
first_res = 1
second_res = 1
height = len(G[0])
for index, (change_up, change_left) in enumerate([(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]):
    pos_up = 0
    pos_left = 0
    res = 0
    while pos_up < len(G)-1:
        pos_up += change_up
        pos_left += change_left
        pos_left %= height
        if pos_up >= len(G):
            break
        if G[pos_up][pos_left] == "#":
            res += 1
    second_res *= res
    if index == 1:
        first_res *= res

print(first_res)
print(second_res)


