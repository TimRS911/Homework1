class Worker:

    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": int(salary), "bonus": int(bonus)}

class Position(Worker):
    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position, salary, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["salary"] + self._income["bonus"]

p = Position('Timur', 'Ismailov', 'developer', '200000', '20000')
print(p.get_full_name(), p.get_total_income())