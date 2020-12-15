DIVIDER = "="
FILE_NAME = "input14.in"


def return_combos(val):
    all = set()

    def rec(index, stringo):
        if index == 36:
            all.add(stringo[:])
            return
        else:
            if val[index] == "1":
                rec(index+1, stringo + "1")
            elif val[index] == "0":
                rec(index + 1, stringo + "0")
            else:
                rec(index+1, stringo + "1")
                rec(index+1, stringo + "0")
    rec(0, "")
    return all


def add_mask(mask, value, first_task):
    res = ""
    for i in range(36):
        if mask[i] == "1":
            res += "1"
        elif mask[i] == "0":
            if first_task:
                res += "0"
            else:
                res += value[i]
        else:
            if first_task:
                res += value[i]
            else:
                res += "X"
    return res


first_memo, second_memo = {}, {}
with open(FILE_NAME, 'r') as file:
    for line in file:
        value = line.strip().split(DIVIDER)
        value[0] = value[0].strip()
        value[1] = value[1].strip()
        if "mask" in value[0]:
            mask = value[1]
        else:
            index = int(value[0][4:-1])
            val = int(value[1])
            first_val = str(bin(int(val))).replace("b", "0")
            second_val = str(bin(int(index))).replace("b", "0")
            first_new_val = first_val.zfill(36)
            second_new_val = second_val.zfill(36)
            first_res = add_mask(mask, first_new_val, True)
            second_res = add_mask(mask, second_new_val, False)
            first_memo[index] = int(first_res, 2)
            alls = return_combos(second_res)
            for so in alls:
                second_memo[int(so, 2)] = int(val)

    print(sum(first_memo.values()))
    print(sum(second_memo.values()))

