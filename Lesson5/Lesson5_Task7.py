# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

# первый вариант, если использовать строки из примера
import json

list_of_firm = []
firm_profit = {}
firm_loss = {}
with open('file_for_Task7.txt', 'r') as file:
    for row in file.readlines():
        split_row = row.split(' ')
        full_profit = 0
        # так как мы знаем что первые два элемента будут наименованием и организационно-правовой формой можем сделать
        # срез
        for num in split_row[2:-1]:
            full_profit += int(num)
        average_profit = full_profit / len(split_row[2:-1])
        firm_profit[split_row[0]] = average_profit
        firm_loss[split_row[0]] = int(split_row[-1])
    list_of_firm.append(firm_profit)
    list_of_firm.append(firm_loss)
print(list_of_firm)
with open('result_file.txt', 'w') as result:
    json.dump(list_of_firm, result)

# второй вариант где строки в виде name firm_1 form ООО profit 10000 9600 85 96 1452000 loss 5000
list_of_firm = []
firm_profit = {}
firm_loss = {}
with open('file_for_Tas7_2.txt', 'r') as file:
    for row in file.readlines():
        split_row = row.split(' ')
        full_profit = 0
        if 'loss' in split_row:
            # так как мы знаем что первые четыре элемента будут наименованием и организационно-правовой формой можем
            # сделать срез
            for num in split_row[5:-2]:
                full_profit += int(num)
            average_profit = full_profit / len(split_row[5:-2])
            firm_loss[split_row[1]] = int(split_row[-1])
        else:
            for num in split_row[6:]:
                full_profit += int(num)
            average_profit = full_profit / len(split_row[6:])
        firm_profit[split_row[1]] = average_profit
    list_of_firm.append(firm_profit)
    list_of_firm.append(firm_loss)
print(list_of_firm)
with open('result_file2.txt', 'w') as result:
    json.dump(list_of_firm, result)
