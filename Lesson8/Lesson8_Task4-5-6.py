# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники. 5. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о
# наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь. 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип
# данных. Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from abc import ABC, abstractmethod
from time import strftime as t
from time import sleep

print('Для помещения вещи на склад, данные записываются в виде : предметы=[принтер,ксерокс,сканер],количество=[5,6,10]')
print('Для выгрузки вещей в определенный пункт назначения, данные записываются в виде: ' + '\n' +
      'предметы=[принтер,ксерокс,сканер],[["место назначения","колличество"],["место назначения","колличество"],' + '\n' +
      '["место назначения","колличество"]]')


class Warehouse:
    data_base = {}

    def accept_goods(self, goods=list, quantity=list):
        if len(goods) == len(quantity):
            for i in range(len(goods)):
                if 'Колличество на складе' in goods[i].__dict__:
                    goods[i].__dict__['Колличество на складе'] = goods[i].__dict__['Колличество на складе'] + quantity[
                        i]
                    self.data_base[goods[i].name] = goods[i].__dict__
                else:
                    goods[i].__dict__['Колличество на складе'] = quantity[i]
                    self.data_base[goods[i].name] = goods[i].__dict__
        else:
            return 'Данные не совпадают, пожалуйста проверьте, что бы наименования товаров и количество были указаны верно'
        return self.data_base

    def to_ship_goods(self, goods=list, quantity_and_place=list):
        if len(goods) == len(quantity_and_place):
            for i in range(len(goods)):
                if self.data_base[goods[i].name]['Колличество на складе'] >= quantity_and_place[i][1]:
                    self.data_base[goods[i].name]['Колличество на складе'] = self.data_base[goods[i].name][
                                                                                 'Колличество на складе'] - \
                                                                             quantity_and_place[i][1]
                    goods[i].__dict__[f'{t("%Y-%m-%d-%H-%M-%S")}'] = 'Отгружено в:' + quantity_and_place[i][
                        0] + 'в колличестве ' + str(
                        quantity_and_place[i][1]) + ' шт.'
                else:
                    print(
                        f'К сожалению сейчас на складе: {goods[i]}, меньше чем требуется({self.data_base[goods[i]]["Колличество на складе"]})')
        else:
            return 'Данные не совпадают, пожалуйста проверьте, что бы наименования товаров и количество_место были указаны верно'
        return self.data_base


class Office_equipment(ABC):
    def __init__(self, price, model, weight):
        self.price = price
        self.model = model
        self.weight = weight

    @abstractmethod
    def work_skills(self):
        pass


class Printer(Office_equipment):
    def __init__(self, price, model, weight, color):
        super().__init__(price, model, weight)
        self.color = color
        self.name = Printer.__name__

    def work_skills(self):
        return 'Я печатаю'


class Scanner(Office_equipment):
    def __init__(self, price, model, weight, speed_of_work):
        super().__init__(price, model, weight)
        self.speed_of_work = speed_of_work
        self.name = Scanner.__name__

    def work_skills(self):
        return 'Я сканирую'


class Xerox(Office_equipment):
    def __init__(self, price, model, weight, life_time):
        super().__init__(price, model, weight)
        self.life_time = life_time
        self.name = Xerox.__name__

    def work_skills(self):
        return 'Я печатаю и сканирую'


printer = Printer(15000, 'rx-500', '10кг', 'красный')
scanner = Scanner(10000, 'md-45s', '7кг', '30л/м')
xerox = Xerox(20000, 'ult56-500', '15кг', '10лет')
warehouse = Warehouse()
print(printer.name, printer.weight)
print(scanner.speed_of_work)
print(xerox.model, xerox.__dict__)
print('Добавляем на склад' + str(warehouse.accept_goods([printer, scanner, xerox], [5, 8, 9])))
print(warehouse.accept_goods([printer, xerox], [5, 8, 9]))
print('Забираем со склада' + str(
    warehouse.to_ship_goods([printer, scanner, xerox], [[' магадан', 5], ['москва', 5], ['Красная площадь', 5]])))
print('Добавляем' + str(warehouse.accept_goods([printer, scanner, xerox], [10, 10, 10])))
sleep(2)
print('Забираем' + str(warehouse.to_ship_goods([scanner, xerox], [['Курск', 7], ['Тула', 6]])))
