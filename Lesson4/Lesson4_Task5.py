# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

#решение через reduce
from functools import reduce

def my_func(first, second):
    return first+second


print(reduce(my_func, (num for num in range(100,1001,2))))

#решение через sum

print(sum((num for num in range(100,1001,2))))