class Car:
    speed = 25
    color = 'Yellow'
    name = 'Porsche'
    is_police = False
    def go(self):
        print('go-go-go')
    def stop(self):
        print('tr-trr-trrr')
    def turn(self, l_or_r):
        print(l_or_r)
    def show_speed(self):
        return self.speed

class TownCar(Car):
    speed = 25
    color = 'yellow'
    name = 'Porsche'
class SportCar(Car):
    speed = 100
    color = 'red'
    name = 'BMW'
class WorkCar(Car):
    speed = 25
    color = 'green'
    name = 'Mazda'
class PoliceCar(Car):
    is_police = True
    speed = 30
    color = 'black'
    name = 'Lada'

t = TownCar()
w = WorkCar()
if t.speed > 60:
    print('Привешение скорости!')
if w.speed > 40:
    print('Привешение скорости!')
print(t.speed)