# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# Решение при помощи регулярных выражений
import re

with open('employees_file.txt') as employees:
    average_sum = 0
    print(employees.readlines())
    for string in employees.readlines():
        result = re.findall(r'\d+\s*\d+', string)
        # из за того что оклады записаны через пробел, приходится делать реплейс, можно было просто в файле изменить
        # но я решил не идти по легкому пути
        try:
            if int(result[0].replace(' ', '')) < 20000:
                print(string.split(' ')[0])
        # обыгрываем ошибку если число записано без пробела
        except IndexError:
            with open('bugs.txt', 'a') as bugs:
                bugs.write('Число было не в виде d_d\n')
            print(string.split(' ')[0])

