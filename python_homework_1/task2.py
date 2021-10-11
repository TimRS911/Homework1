user_sec = int(input('Введите количество секунд: '))

hour = user_sec // 3600
min = (user_sec - 3600 * hour) // 60
sec = (user_sec - 3600 * hour) % 60

print(f'{hour:02}:{min:02}:{sec:02}')
