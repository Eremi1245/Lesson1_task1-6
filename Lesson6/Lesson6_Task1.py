# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
# Продолжительность первого состояния (красный) 
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
#  Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, 
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
from datetime import datetime
from time import sleep


# если стартовый свет задается изначально
class TrafficLight:
    _color = 'красный'

    def running(self, count_of_traffic):
        count = 1
        while count <= count_of_traffic:
            print(f'Круг: {count}')
            TrafficLight._color = 'красный'
            print(f'{TrafficLight._color}({datetime.now().strftime("%H-%M-%S")})')
            sleep(7)
            TrafficLight._color = 'желтый'
            print(f'{TrafficLight._color}({datetime.now().strftime("%H-%M-%S")})')
            sleep(2)
            TrafficLight._color = 'зеленый'
            print(f'{TrafficLight._color}({datetime.now().strftime("%H-%M-%S")})')
            sleep(7)
            TrafficLight._color = 'желтый'
            print(f'{TrafficLight._color}({datetime.now().strftime("%H-%M-%S")})')
            sleep(2)
            count += 1
        print('Стоп')


Svetof = TrafficLight()
print(Svetof._color)
Svetof.running(2)


# если стартовый свет задается пользователем
class TrafficLight:
    dict_for_colors = {'красный': 7, 'желтый': 2, 'зеленый': 5}

    def __init__(self, color):
        if color not in TrafficLight.dict_for_colors.keys():
            raise KeyError(f'Свет светофора должен быть одним из этих цветов: {TrafficLight.dict_for_colors.keys()}')
        self._color = color

    def work_of_TrafficLight(self, list_of_colors, circle):
        count = 1
        while count <= circle:
            for color in list_of_colors:
                self._color = color
                print(f'{color}({datetime.now().strftime("%H-%M-%S")})')
                sleep(TrafficLight.dict_for_colors[color])
            count += 1

    def running(self, count_of_traffic=int):
        if self._color == 'красный':
            self.work_of_TrafficLight(['красный', 'желтый', 'зеленый', 'желтый'], count_of_traffic)
        elif self._color == 'желтый':
            self.work_of_TrafficLight(['желтый', 'зеленый', 'желтый', 'красный'], count_of_traffic)
        elif self._color == 'зеленый':
            self.work_of_TrafficLight(['зеленый', 'желтый', 'красный', 'желтый'], count_of_traffic)
        print('Стоп')


Svetof = TrafficLight('красный')
print(Svetof._color)
Svetof.running(2)
Svetof = TrafficLight('желтый')
print(Svetof._color)
Svetof.running(2)
Svetof = TrafficLight('зеленый')
print(Svetof._color)
Svetof.running(2)
Svetof = TrafficLight('оранжевый')
print(Svetof._color)
Svetof.running(2)
