FILE_NAME = "input10.in"

with open(FILE_NAME, 'r') as file:
    vals = sorted([int(line.strip()) for line in file])

one, three = 0, 0
cur = 0
maxo = (vals[-1] + 3)
vals.append(maxo)

for i in range(len(vals)):   #part 1
    if vals[i] - cur == 1:
        one += 1
    elif vals[i] - cur == 3:
        three += 1
    cur = vals[i]

print(one * three)

val_seto = set(vals)

dp = [0 for _ in range(max(vals))]  #part 2
dp[0] = 1
dp[1] = 1 if 1 in val_seto else 0
dp[2] = 0 if 2 not in val_seto else dp[0] + dp[1]

for i in range(3, max(vals)):
    value = i
    if value not in val_seto:
        dp[i] = 0
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

print(max(dp))


