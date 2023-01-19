def get_cook_book(file_name):
    with open(file_name, 'rt', encoding = 'utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line.strip()
            indredients_count = int(f.readline())
            ingredients = []
            for i in range (indredients_count):
                ing = f.readline().strip()
                ingredient_name, quantity, measure = ing.split('|')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            f.readline()
            cook_book[dish_name] = ingredients
    return cook_book
print(get_cook_book("recipes.txt"))

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book(input('Введите название кулинарной книги '))
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            product = dict(ingredient)
            product['quantity'] *= person_count
            if product['ingredient_name'] not in shop_list:
                shop_list[product['ingredient_name']] = {'measure': product['measure'], 'quantity': product['quantity']}
            else:
                shop_list[product['ingredient_name']]['quantity'] += product['quantity']
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))