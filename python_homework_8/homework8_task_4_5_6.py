class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Наименование': self.name, 'Цена': self.price, 'Количество': self.quantity}

    def income(self):
        try:
            name = input(f'Введите наименование: ')
            price = int(input(f'Введите цену за ед: '))
            quantity = int(input(f'Введите количество: '))
            item = {'Наименование': name, 'Цена': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)

        except ValueError:
            print('Недопустимое значение.')


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Copier(OfficeEquipment):
    pass


p = Printer('HP', 4000, 23)
s = Scanner('Canon', 2100, 11)
c = Copier('Xerox', 6430, 4)
p.income()
s.income()
c.income()

