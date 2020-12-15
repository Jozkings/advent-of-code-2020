from sympy.ntheory.modular import crt

FILE_NAME = "input13.in"


with open(FILE_NAME, 'r') as file:
    first = True
    for line in file:
        if first:
            depart = int(line)
            first = False
        else:
            vals = line.split(",")

min_time, min_index = None, None
for index, val in enumerate(vals):   #part 1
    if val == "x":
        continue
    valo = int(val)
    divisor = depart // valo
    timo = (divisor + 1) * valo
    diff = timo - depart
    if min_time is None or diff < min_time:
        min_time = diff
        min_index = index

print(min_time * int(vals[min_index]))

dicto = {}
for i in range(len(vals)):  #part 2
    value = vals[i]
    if value != "x":
        dicto[int(value)] = int(value) - i

print(crt(dicto.keys(), dicto.values())[0])




