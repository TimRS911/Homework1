my_name = 'Тимур'

print('Привет! Меня зовут ' + my_name + '. А как тебя зовут?')
user_name = input()

print(user_name + ', а сколько тебе лет?')
user_age = int(input())
my_age = 35

if user_age < my_age:
    print('Я старше тебя.')
elif user_age == my_age:
    print('Мы ровесники.')
else:
    print('Ты старше меня.')
    