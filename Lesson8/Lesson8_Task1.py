# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class UserDate:
    usersdate = ''

    def __init__(self, usersdate):
        UserDate.usersdate = usersdate

    @classmethod
    def usersdate_to_int(cls):
        split_data = cls.usersdate.split('-')
        cls.int_usersdate = [int(num) for num in split_data]
        return cls.int_usersdate

    @staticmethod
    def valid_atributes():
        if 32 > UserDate.int_usersdate[0] > 0:
            print('Число описывающее день, записано верно')
        else:
            print('Число описывающее день, имеет не возможное значение')
        if 13 > UserDate.int_usersdate[1] > 0:
            print('Число описывающее месяц, записано верно')
        else:
            print('Число описывающее месяц, имеет не возможное значение')
        if len(str(UserDate.int_usersdate[2])) == 4:
            print('Число описывающее год, записано верно')
        else:
            print('Число описывающее год, имеет не возможное значение')


cl = UserDate('04-11-2020')

print(cl.usersdate_to_int())
cl.valid_atributes()
