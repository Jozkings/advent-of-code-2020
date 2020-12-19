from collections import defaultdict


FILE_NAME = "input19.in"

with open(FILE_NAME, 'r') as file:
    rules_bool = True
    rules, messages = defaultdict(list), []
    for line in file:
        if line == "\n":
            rules_bool = False
            continue
        if rules_bool:
            values = line.strip().split(": ")
            key, decoders = int(values[0]), values[1:][0]
            if '"' in decoders:
                rules[key] = decoders
            else:
                alls, news = [], []
                for value in decoders.split(" "):
                    if value != "|" and value != "":
                        news.append(int(value))
                    else:
                        alls.append(news)
                        news = []
                alls.append(news)
                rules[key] = alls
        else:
            messages.append(line.strip())


def rec_matching(string, chars):
    if not chars and not string:
        return True
    if not chars or not string:
        return False

    character = chars[0]
    if type(character) == str and string[0] == character:
        return rec_matching(string[1:], chars[1:])
    for rule in rules[character]:
        if rec_matching(string, list(rule) + chars[1:]):
            return True
    return False


def solve(rules):
    good = 0
    for message in messages:
        good += rec_matching(message, rules[0][0])
    return good


print(solve(rules))
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
print(solve(rules))
