FILE_NAME = "input6.in"

with open(FILE_NAME, 'r') as file:
    first_seto, second_seto = set(), set()
    first_suma, second_suma = 0, 0
    new = True
    for line in file:
        value = line.strip()
        if not value:
            first_suma += len(first_seto)
            second_suma += len(second_seto)
            first_seto, second_seto = set(), set()
            new = True
        else:
            current_seto = set()
            for val in value:
                current_seto.add(val)
            if new:
                second_seto = current_seto
                new = False
            else:
                second_seto &= current_seto
            first_seto |= current_seto
    first_suma += len(first_seto)
    second_suma += len(second_seto)
    print(first_suma)
    print(second_suma)





