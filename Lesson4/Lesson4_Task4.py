# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. 
# Сформировать итоговый массив чисел, соответствующих требованию. 
# Элементы вывести в порядке их следования в исходном списке. 
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

# c классом Counter
from collections import Counter

user_list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def gen_without_double_num(user_list):
    count = Counter(user_list)
    for item in count:
        if count[item] >= 2:
            continue
        else:
            yield item


result_gener = gen_without_double_num(user_list1)
for i in result_gener:
    print(i)
print('Следующий вариант')


# без Counter
def gen_without_double_num(user_list):
    for i in user_list:
        count = 0
        for j in user_list:
            if i == j:
                count += 1
            else:
                continue
        if count >= 2:
            continue
        else:
            yield i


result_gener2 = gen_without_double_num(user_list1)
for i in result_gener2:
    print(i)
