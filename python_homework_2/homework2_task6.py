article_list = []
article_num = 1
command = ''
while command != 'stop':
    name = input('name: ')
    price = input('price: ')
    amount = input('amount: ')
    units = input('units: ')
    article_list.append((article_num, {'name': name, 'price': price, 'amount': amount, 'units': units}))
    article_num += 1
    command = input('Напишите stop для окончания: ')

result_list = {}
for numb, prod_dict in article_list:
    for key, value in prod_dict.items():
        if not result_list.get(key):
            result_list[key] = [value]
        else:
            result_list[key].append(value)
for key, value in result_list.items():
    result_list[key] = list(set(value))

print(result_list)