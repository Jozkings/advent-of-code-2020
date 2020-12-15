FILE_NAME = "input9.in"

with open(FILE_NAME, 'r') as file:
    vals = [int(line.strip()) for line in file]


for index, value in enumerate(vals):    #first part
    if index >= 25:
        suc = False
        for i in range(index-25, index):
            if suc:
                break
            for j in range(index-25, index):
                if i != j and vals[i] + vals[j] == value:
                    suc = True
                    break
        if not suc:
            INVALID = value
            break

print(INVALID)
contiguous_res = None

for i in range(len(vals)-1):
    if contiguous_res:
        break
    for j in range(i+1, len(vals)):
        if contiguous_res:
            break
        if sum(vals[i:j+1]) == INVALID:
            contiguous_res = min(vals[i:j+1]) + max(vals[i:j+1])

print(contiguous_res)




