x = float(input('Введите положительное число X: '))
y = int(input('Введите целое отрицательное число Y: '))

method_1 = x ** y
print(method_1)

def method_2(x, y):
    if x < 0:
        return 'X должен быть положительным числом!'
    if y > 0:
        return 'Y должен быть отрицательным числом!'
    z = 1
    for i in range(y * -1):
        z *= x
    return 1 / z
print(method_2(x, y))
