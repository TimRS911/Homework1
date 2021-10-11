earn = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издерек: '))
income = earn - costs
profit = income / earn

if earn > costs:
    print('Отлично! Вы работаете в прибыль.')
    print('Ваша рентабельность: ' + str(profit))
elif earn == costs:
    print('Вы работаете в ноль.')
else:
    print('Увы! Вы работаете в убыток.')

staff = int(input('Введите количество сотрудников: '))

print('Прибыль фирмы на одного сотрудника: ' + str(income / staff))
