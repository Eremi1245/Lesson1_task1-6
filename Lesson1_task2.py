# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
users_input = int(input('Введите время в секундах'))
if users_input > 3600:
    hours = users_input // 3600
    hours_remainder = users_input % 3600
    if hours_remainder > 60:
        minutes = hours_remainder//60
        seconds = hours_remainder % 60
    else:
        seconds = hours_remainder
else:
    hours = 0
    if users_input > 60:
        minutes = users_input//60
        seconds = users_input % 60
    else:
        minutes = 0
        seconds = users_input

print('%02d:%02d:%02d' % (hours, minutes, seconds))