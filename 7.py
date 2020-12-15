from collections import defaultdict

FILE_NAME = "input7.in"

with open(FILE_NAME, 'r') as file:
    bags = defaultdict(set)
    for line in file:
        value = line.strip().split()
        bag = value[:2]
        for i in range(2, len(value)):
            char = value[i]
            if char == "contain":
                if value[i+1] == "no":
                    bags[" ".join(bag)] = set()
                    break
                new = value[i+1:i+4]
                bags[" ".join(bag)].add(" ".join(new))
            elif char == "," or char == "bag," or char == "bags,":
                new = value[i + 1:i + 4]
                bags[" ".join(bag)].add(" ".join(new))

    goods = set()
    lengtho = -1

    while lengtho != len(goods):   #part 1
        lengtho = len(goods)
        for bag in bags.keys():
            for value in bags[bag]:
                if "shiny gold" in value:
                    goods.add(bag)
                elif " ".join(value.split()[1:]) in goods:
                    goods.add(bag)
    print(len(goods))

    res = -1
    currents = [("shiny gold", 1)]
    while currents:          #part 2
        current, numo = currents.pop(0)
        res += numo
        for val in bags[current]:
            if val:
                number = int(val.split()[0])
                currents.append((" ".join(val.split()[1:]), numo*number))
    print(res)








