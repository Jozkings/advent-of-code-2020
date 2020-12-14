FILE_NAME = "input2.in"
DIVIDER = ","

with open(FILE_NAME, 'r') as file:
    valids = 0
    values = [line.strip().split() for line in file]

first_valids = 0
second_valids = 0

for val in values:
    rango, what, passw = val
    what = what[0]
    fr, sr = map(int, rango.split("-"))
    occurence = 0
    times = 0
    for i in range(len(passw)):
        character = passw[i]
        if character == what:
            occurence += 1
            if i+1 == fr or i+1 == sr:
                times += 1
    first_valids += (fr <= occurence <= sr)
    second_valids += (times == 1)
print(first_valids)
print(second_valids)


