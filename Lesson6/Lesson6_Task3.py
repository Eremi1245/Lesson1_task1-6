# 3. Реализовать базовый класс Worker (работник), 
# в котором определить атрибуты: name, surname, position (должность), income (доход). 
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
# оклад и премия, например, {"wage": wage, "bonus": bonus}. 
# Создать класс Position (должность) на базе класса Worker. 
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных 
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
ivanov_income = {"wage": 150000, "bonus": 20000}
petrov_income = {"wage": 15000, "bonus": 200000}
sidorov_income = {"wage": 160000, "bonus": 20}


class Worker:
    def __init__(self, name, surname, position, income=dict):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self, mounth):  # добавил умножение дохода на время работы
        return mounth * (self._Worker__income['wage'] + self._Worker__income['bonus'])


ivanov = Position('Ivanov', 'Alexander', 'lawyer', ivanov_income)
petrov = Position('Petrov', 'Artem', 'accountant', petrov_income)
sidorov = Position('Sidorov', 'Roma', 'programmer', sidorov_income)
print(ivanov.get_full_name(), ivanov.get_total_income(5))
print(petrov.get_full_name(), petrov.get_total_income(5))
print(sidorov.get_full_name(), sidorov.get_total_income(5))
