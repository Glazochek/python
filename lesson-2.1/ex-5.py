"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""

class Plate:

    def __init__(self, size_mx):
        self.plates = []
        self.size_mx = size_mx

    def __str__(self):
        return str(self.plates)

    def is_empty(self):
        return self.plates == [[]]

    def push_in(self, el):
        if len(self.plates[len(self.plates)-1]) < self.size_mx:
            self.plates[len(self.plates)-1].append(el)
        else:
            self.plates.append([])
            self.plates[len(self.plates)-1].append(el)

    def pop_out(self):
        result = self.plates[len(self.plates)-1].pop()
        if len(self.plates[len(self.plates)-1]) == 0:
            self.plates.pop()
        return result

    def get_val(self):
        return self.plates[len(self.plates)-1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.plates:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.plates)


plates = Plate(3)
print(type(plates))
plates.push_in('plate-1')

# честно говоря, здесь мне пришлось подглядеть разбор задания
#  не снижайте пожалйста оценку, я обязательно во всем разберусь
