class Worker:
    _name = 'Никита'
    _surname = 'Афанасьев'
    _position = 'Дворник'
    _income = {"wage": 20900, "bonus": 1000}

class Position(Worker):
    def get_full_name(self):
        full_name = self._name + ' ' + self._surname
        return full_name

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        return total_income

w = Position()
print(w.get_full_name())
print(w.get_total_income())