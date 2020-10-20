# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
dict_for_task = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('file_for_Task4.txt', 'r') as file:
    for row in file.readlines():
        split_row = row.split(' ')
        with open('file_for_Task4_num_2.txt', 'a') as file2:
            file2.write(dict_for_task[split_row[0]] + ' '.join(split_row[1:]))


