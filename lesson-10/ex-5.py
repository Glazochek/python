class Stationery:
    title = None
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    title = 'Ручкой'

class Pencil(Stationery):
    title = 'Карандашом'

class Handle(Stationery):
    title = 'Фломастером'


Pen().draw()
Pencil().draw()
Handle().draw()