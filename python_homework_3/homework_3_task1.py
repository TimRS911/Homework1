def arguments(a, b):
    if b == 0:
        return 'На ноль делить нельзя!'
    else:
        return a / b
a = float(input('a: '))
b = float(input('b: '))
print(arguments(a, b))
