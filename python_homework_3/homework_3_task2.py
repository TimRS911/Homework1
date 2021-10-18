name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
year = input('Введите ваш год рождения: ')
city = input('Введите ваш город проживания: ')
mail = input('Введите ваш e-mail: ')
phone = input('Введите ваш номер телефона: ')

def user_data(name, surname, year, city, mail, phone):
    print(f'{name} {surname} {year} {city} {mail} {phone}')
user_data(name=name, surname=surname, year=year, city=city, mail=mail, phone=phone)
