from collections import defaultdict

inputo = [6,13,1,15,2,0]

index = 1
spoken = defaultdict(int)
inputo_index = 0
while index != 30000001:  #first part 2021
    if inputo_index != len(inputo):
        spoken[inputo[inputo_index]] = index
        said = inputo[inputo_index]
        to_be_said = 0
        inputo_index += 1
    else:
        said = to_be_said
        if to_be_said in spoken:
            to_be_said = index - spoken[to_be_said]
        else:
            to_be_said = 0
        spoken[said] = index
    index += 1
print(said)

