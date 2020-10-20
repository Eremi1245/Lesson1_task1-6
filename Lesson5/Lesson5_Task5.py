# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('Test_file_for_task6.txt', 'w') as file:
    file.write('568 65819 953 8 6 7 95 314 6')
with open('Test_file_for_task6.txt', 'r') as file:
    split_num = file.readline().split(' ')
    result_sum = 0
    for num in split_num:
        result_sum += int(num)
    print(result_sum)
