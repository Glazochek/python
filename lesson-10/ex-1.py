import time
class TrafficLigh:
    __color = None
    def running(self):
        self.__color = 'красный'
        print(self.__color)
        time.sleep(7)
        self.__color = 'желтый'
        print(self.__color)
        time.sleep(2)
        self.__color = 'зеленый'
        print(self.__color)
        time.sleep(7)

a = TrafficLigh()
a.running()
