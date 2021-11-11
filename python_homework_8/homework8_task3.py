class MyError(Exception):
    def __init__(self):
        pass

class TypeCheck:
    def __init__(self):
        self.user_list = []

    def check_value(self):
        global user_num
        while True:
            try:
                try:
                    user_num = int(input('Введите числo: '))
                    ex = input('Добавлено в список. Продолжить? y/n: ')
                    self.user_list.append(user_num)
                    if ex == 'n':
                        print(self.user_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input('Это не число. Продолжить? y/n: ')
                if ex == 'n':
                    print(self.user_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()
