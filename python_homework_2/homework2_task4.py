user_str = input('Введите строку из нескольких слов: ')

words_list = user_str.split()
for num, word in enumerate(words_list):
    print(f'{num} - {word[:10]}')