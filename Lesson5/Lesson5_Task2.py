# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
# выполнить подсчет количества строк, количества слов в каждой строке.

# Используем файл из первого задания
len_of_words = {}
with open('Test_file1.txt') as file:
    for word in file.readlines():
        len_of_words[word] = len(word.split(' '))
print(f'Колличество строк- {len(len_of_words.keys())}, колличество слов в каждой строке- {len_of_words}')
