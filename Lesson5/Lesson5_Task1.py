# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных свидетельствует пустая строка.
users_text = []
print('Для окончания ввода данных, введите пустую строку')
while True:
    user_input = input('Введите данные которые хотите записать в строку текстового файла: ')
    if user_input == '':
        break
    users_text.append(user_input)

with open('Test_file1.txt', 'w') as file:
    for row in users_text:
        file.write(row + '\n')
# проверка
with open('Test_file1.txt') as file:
    for i in file.readlines():
        print(i)
