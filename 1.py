FILE_NAME = "input1.in"

with open(FILE_NAME, 'r') as file:
    vals = [int(line.strip()) for line in file]

for i, val1 in enumerate(vals):
    for j, val2 in enumerate(vals[i+1:]):
        if val1 + val2 == 2020:
            print(f'First part: {val1 * val2}')
        for val3 in vals[i+j+1:]:
            if val1 + val2 + val3 == 2020:
                print(f'Second part: {val1 * val2 * val3}')


