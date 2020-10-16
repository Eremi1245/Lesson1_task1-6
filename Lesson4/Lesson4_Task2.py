# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

# не понял что значит использовать генератор для формирования списка,
# поэтому сделал варианты с формированием генератора и формированием списка
start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
another_list = [100, 5, 85, 65, 96, 110, 885, 1, 5, 7, 6]


def gener_for_list(list_for_check):
    for i in range(len(list_for_check) - 1):
        if list_for_check[i] < list_for_check[i + 1]:
            yield (list_for_check[i + 1])


result = gener_for_list(start_list)
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
result2 = gener_for_list(another_list)
print(result2)
print(next(result2))
print(next(result2))
print(next(result2))
print(next(result2))
print(next(result2))
print(next(result2))

result3 = [start_list[i + 1] for i in range(len(start_list) - 1) if start_list[i] < start_list[i + 1]]
result4 = [another_list[i + 1] for i in range(len(another_list) - 1) if another_list[i] < another_list[i + 1]]
print(result3)
print(result4)
