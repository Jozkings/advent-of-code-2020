from collections import defaultdict

FILE_NAME = "input4.in"

all_fields = {'pid', 'byr', 'hgt', 'iyr', 'hcl', 'eyr', 'cid', 'ecl'}
res = 0


def good_hair(color):
    for char in color:
        if ("a" <= char <= "f") or ("0" <= char <= "9"):
            return True
    return False


def check_pid(number):
    if len(number) != 9:
        return False
    for char in number:
        if "0" <= char <= "9":
            continue
        return False
    return True


def check_passport(dict_):
    good = 0
    for key, value in dict_.items():
        if not value:
            break
        if key == "byr":
            good += 1920 <= int(value) <= 2002
        elif key == "iyr":
            good += 2010 <= int(value) <= 2020
        elif key == "eyr":
            good += 2020 <= int(value) <= 2030
        elif key == "hgt":
            metric = value[-2:]
            if metric == "cm":
                good += 150 <= int(value[:-2]) <= 193
            elif metric == "in":
                good += 59 <= int(value[:-2]) <= 76
        elif key == "hcl":
            good += (len(value) == 7 and value[0] == "#" and good_hair(value[1:]))
        elif key == "ecl":
            good += value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        elif key == "pid":
            good += check_pid(value)
    return good == 7


with open(FILE_NAME, 'r') as file:
    values = [line.strip().split() for line in file]

all_fields_res = 0
fields = set()
currents = defaultdict(str)
for value in values:
    if not value:
        if fields == all_fields or fields == all_fields - {"cid"}:
            all_fields_res += 1
            res += check_passport(currents)
        fields = set()
        currents = defaultdict(str)
    else:
        fields |= set(val.split(":")[0] for val in value)
        for val in value:
            first, second = val.split(":")
            currents[first] = second

print(all_fields_res + 1 if (fields == all_fields or fields == all_fields - {"cid"}) else all_fields_res)
print(res + 1 if check_passport(currents) else res)





