# . Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов. min max
def my_func(a,b,c):
    args_list=[a,b,c]
    return sum(args_list)-min(args_list)
print(my_func(10,8,6))