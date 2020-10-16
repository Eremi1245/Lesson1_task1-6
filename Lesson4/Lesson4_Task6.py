# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


# a) с count

from itertools import count

for item in count(3):
    if item > 10:
        break
    else:
        print(item)


# a) без count
def func_without_count(start, finish):
    return [num for num in range(start, finish + 1)]


it = iter(func_without_count(3, 10))
print(type(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# б) с cycle

from itertools import cycle

сount = 0
for item in cycle("ABC"):
    if сount > 10:
        break
    print(item)
    сount += 1
# без cycle

user_list = ['A', 'B', 'C']
count = 0
while count < 10:
    user_list.append(user_list[count])
    count += 1
print(user_list)
