class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        user_num_1 = int(input('Введите число: '))
        user_num_2 = int(input('Введите второе число (кроме 0): '))
        if user_num_2 == 0:
            raise OwnError('На 0 делить нельзя')
        else:
            res = user_num_1 / user_num_2
            return res
    except ValueError:
        return 'Это не число'
    except OwnError as err:
        return err


print(div())
