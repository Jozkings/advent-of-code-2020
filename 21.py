from collections import defaultdict

DIVIDER = " (contains "
FILE_NAME = "input21.in"

ingredients = defaultdict(set)
allergens = defaultdict(set)

with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        value = line.strip().split(DIVIDER)
        if value[1]:
            value[1] = value[1][:-1]
        for val in value[0].split(" "):
            ingredients[val].add(index)
        for val in value[1].split(", "):
            allergens[val].add(index)

save = set()
for ingredient, ing_indeces in ingredients.items():
    bad = False
    for allergen, aller_indeces in allergens.items():
        if aller_indeces & ing_indeces == aller_indeces:
            bad = True
            break
    if not bad:
        save.add(ingredient)

print(sum([len(ingredients[save_ingredient]) for save_ingredient in save]))

bad_ingredients = [ingredient for ingredient in ingredients if ingredient not in save]
bad_allergens = list(allergens.keys())


def is_correct(chosen_map):
    for ingredient, allergen in chosen_map.items():
        res = ingredients[bad_ingredients[ingredient]] & allergens[bad_allergens[allergen]]
        if res != allergens[bad_allergens[allergen]]:
            return False
    return True


def print_second_result(result_map):
    result_tuples = sorted([(bad_ingredients[key], bad_allergens[value]) for key, value in result_map.items()], key = lambda val:val[1])
    result = ""
    for ingredient, _ in result_tuples:
        result += f'{ingredient},'
    print(result[:-1])


def rec(chosen, left_ingredients, left_allergens):
    if not left_ingredients:
        if is_correct(chosen):
            print_second_result(chosen)
            return True
    for ingredient_index in left_ingredients:
        allergen = left_allergens.pop(-1)
        chosen[ingredient_index] = allergen
        finished = rec(chosen, left_ingredients - {ingredient_index}, left_allergens)
        if finished:
            return True
        left_allergens.append(allergen)
        del chosen[ingredient_index]
    return False


rec(dict(), set([i for i in range(len(bad_ingredients))]), [i for i in range(len(bad_ingredients))])