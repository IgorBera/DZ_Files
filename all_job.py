# Задание №1
with open("recipes.txt", "r") as f:
    cook_book = {}
    while True:
        dish = f.readline().rstrip()
        if not dish:
            break
        amount = int(f.readline())
        cook_book[dish] = []
        for _ in range(amount):
            line = f.readline().rstrip().split(' | ')
            cook_book[dish].append({
                'ingredient_name': line[0],
                'quantity': int(line[1]),
                'measure': line[2]
            })
        f.readline()


# Задание №2
def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in ingredients:
                ingredients[ingredient['ingredient_name']]['quantity'] = \
                    ingredients[ingredient['ingredient_name']]['quantity'] \
                    + ingredient['quantity'] * person_count
            else:
                ingredients[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
    return ingredients


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))


# Задание №3
import os

sort_name, name_text = {}, {}

for filename in os.listdir("files"):
    with open(os.path.join("files", filename), 'r') as f:
        text = f.readlines()
        sort_name[filename] = len(text)
        name_text[filename] = text

sort_name = dict(sorted(sort_name.items(), key=lambda x: x[1]))

with open('sort_file.txt', 'w') as f:
    for k, v in sort_name.items():
        f.write(f"{k}\n")
        f.write(f"{v}\n")
        for line in name_text[k]:
            f.write(f"{line.rstrip()}\n")
