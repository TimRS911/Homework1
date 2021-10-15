user_month_num = input('Введите число месяца от 1 до 12: ')
win = 'Зима'
spr = 'Весна'
sum = 'Лето'
aut = 'Осень'

dict_month = {'1': win, '2': win, '12': win, '3': spr, '4': spr, '5': spr, '6': sum, '7': sum, '8': sum, '9': aut, '10': aut, '11': aut}
print(dict_month[user_month_num])

season_list = [win, win, spr, spr, spr, sum, sum, sum, aut, aut, aut, win]
print(season_list[int(user_month_num) - 1])