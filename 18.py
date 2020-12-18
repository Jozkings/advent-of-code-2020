FILE_NAME = "input18.in"


class Custom:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Custom(self.value + other.value)

    def __mul__(self, other):
        return Custom(self.value + other.value)

    def __sub__(self, other):
        return Custom(self.value * other.value)


with open(FILE_NAME, 'r') as file:
    first_res, second_res = Custom(0), Custom(0)
    for line in file:
        new_line = line
        for number in range(0, 10):
            new_line = new_line.replace(f'{number}', f'C({number})')
        first_line = new_line.replace("*", "-")
        second_line = first_line.replace("+", "*")
        first_res += eval(first_line, {"C": Custom})
        second_res += eval(second_line, {"C": Custom})

print(first_res.value)
print(second_res.value)

