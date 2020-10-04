# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
user_input = input('Введите число')
first_var = int(user_input)
second_var = int(user_input+user_input)
third_var = int(user_input+user_input+user_input)
sum_vars = first_var+second_var+third_var
print(sum_vars)
