from pprint import pprint

def cook_book():
    with open('recipe.txt', encoding='utf-8') as file:
        cook_book = {}

        for line in file:
            dish = line.strip()
            count = int(file.readline())
            ingredients = []

            for _ in range(count):
                ing_name, quantity, measure = file.readline().strip().split(' | ')
                ing = {'ingredient_name': ing_name, 'quantity': quantity, 'measure': measure}
                ingredients.append(ing)
            file.readline()
            cook_book[dish] = ingredients
    return cook_book    
# pprint(cook_book(), sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    ing_list = {}
    for dish in dishes:
        for ingredients in cook_book()[dish]:
            i = {}
            if ingredients['ingredient_name'] in ing_list:
                ing_list[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity']) * person_count
            else:
                i['quantity'] = int(ingredients['quantity']) * person_count
                i['measure'] = ingredients['measure']
                ing_list[ingredients['ingredient_name']] = i
    return ing_list

pprint(get_shop_list_by_dishes(dishes=['Фахитос', 'Омлет'], person_count=5), sort_dicts=False)