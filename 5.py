FILE_NAME = "input5.in"

first_res = 0
with open(FILE_NAME, 'r') as file:
    passes = [line.strip() for line in file]

first_res = 0

for i in range(len(passes)):
    passes[i] = passes[i].replace("F", "0")
    passes[i] = passes[i].replace("B", "1")
    passes[i] = passes[i].replace("R", "1")
    passes[i] = passes[i].replace("L", "0")
    bpass_row = int(passes[i][:-3], 2)
    bpass_column = int(passes[i][-3:], 2)
    id = bpass_row * 8 + bpass_column
    passes[i] = id
    first_res = max(first_res, id)

print(first_res)
for i in range(len(passes)-1):
    first = passes[i]
    second = first + 2
    if second in passes and first + 1 not in passes:
        print(first + 1)
        break
    second = first - 2
    if second in passes and first - 1 not in passes:
        print(first - 1)
        break


