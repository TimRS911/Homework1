user_num = int(input('Введите целое положительное число: '))
max_figure = user_num % 10
user_num = user_num // 10

while user_num > 0:
    if user_num % 10 > max_figure:
        max_figure = user_num % 10
    user_num = user_num // 10

print(max_figure)
