# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
user_input = input('Введите число ')
max_num = 0
for num in user_input:
    if int(num) > max_num:
        max_num = int(num)
print(max_num)
