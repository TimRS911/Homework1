my_list = [7, 5, 3, 3, 2]
rating_num = int(input('Введите номер рейтинга: '))
inserted = False
for index, elem in enumerate(my_list):
    if rating_num > elem:
        my_list.insert(index, rating_num)
        inserted = True
        break

if not inserted:
    my_list.append(rating_num)

print(my_list)