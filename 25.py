CARD_PUBLIC_KEY = 16915772
DOOR_PUBLIC_KEY = 18447943
SUBJECT_NUMBER = 7
DIVIDING = 20201227

card_loop_size = 0
value = 1
while value != CARD_PUBLIC_KEY:
    value *= SUBJECT_NUMBER
    value %= DIVIDING
    card_loop_size += 1

res = 1
for i in range(card_loop_size):
    res *= DOOR_PUBLIC_KEY
    res %= DIVIDING

print(res)


door_loop_size = 0              #final check
value = 1
while value != DOOR_PUBLIC_KEY:
    value *= SUBJECT_NUMBER
    value %= DIVIDING
    door_loop_size += 1

second_res = 1
for i in range(door_loop_size):
    second_res *= CARD_PUBLIC_KEY
    second_res %= DIVIDING

print(res == second_res)