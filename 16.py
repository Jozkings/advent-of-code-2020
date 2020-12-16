from collections import defaultdict

FILE_NAME = "input16.in"

fields = defaultdict(list)
your_ticket = []
other_tickets = defaultdict(list)

with open(FILE_NAME, 'r') as file:
    fieldos = True
    your = False
    other = False
    other_index = 0
    for line in file:
        if line == "\n":
            continue
        if "your" in line:
            fieldos = False
            your = True
            continue
        if "nearby" in line:
            other = True
            your = False
            continue
        if fieldos:
            value = line.strip().split(": ")
            key, ranges = value
            first_range, second_range = ranges.split(" or ")
            fields[key].append(first_range)
            fields[key].append(second_range)
        else:
            value = line.strip().split(",")
            if your:
                your_ticket = list(map(int, value))
            if other:
                other_tickets[other_index] = list(map(int, value))
                other_index += 1

invalids = 0
new_others = defaultdict(list)
bad = False

for key, value in other_tickets.items():   #PART 1
    bad = False
    for val in value:
        some_good = False
        for _, conditions in fields.items():
            if some_good:
                break
            for cond in conditions:
                lower, upper = map(int, cond.split("-"))
                if lower <= val <= upper:
                    some_good = True
                    break
        if not some_good:
            invalids += val
            bad = True
    if not bad:
        new_others[key] = value

print(invalids)

fields_options = [set() for _ in range(len(fields))]   #PART 2
help_index = -1
for key, value in new_others.items():    #create  array, each row index represents sets of possibilities of fields for ticket index (1-20)
    help_index += 1
    for index, val in enumerate(value):
        possible_conds = set()
        for condition, ranges in fields.items():
            good = False
            for rango in ranges:
                lower, upper = map(int, rango.split("-"))
                if lower <= val <= upper:
                    good = True
            if good:
                possible_conds.add(condition)
        if help_index == 0:
            fields_options[index] = possible_conds
        else:
            fields_options[index] &= possible_conds

real_positions = [None for _ in range(len(fields))]

while None in real_positions:    #determine position of each field
    to_be_deleted = set()
    for index, conds in enumerate(fields_options):
        if len(conds) == 0:
            continue
        if len(conds) == 1:
            what = next(iter(conds))
            real_positions[index] = what
            to_be_deleted.add(what)
    for val in to_be_deleted:
        for i in range(len(fields_options)):
            if val in fields_options[i]:
                fields_options[i].remove(val)

res = 1
for index, value in enumerate(real_positions):  #get result of 2.part
    if "departure" in value:
        res *= your_ticket[index]
print(res)











