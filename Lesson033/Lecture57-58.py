# Сделать генератор текста на основе статистики.
# Идея проста: подсчитать какие буквы наиболее часто стоят рядом.
# Точнее, подсчитаем как часто за буквой X идёт буква Y, на основе некоего текста.
# После этого начнём с произвольной буквы и каждую следующую будем выбирать
# в зависимости от частоты её появления в статистике

# Для работы с zip архивами, можно использовать модуль zipfile.
# import pprint
import zipfile
from random import randint

zipfile_name = 'sometext.zip'
# С помощью команды zipfile.ZipFile, файл открывается и закрывается???
zip_file = zipfile.ZipFile(zipfile_name, 'r')
# Показывает какие файлы лежат в архиве (+ когда изменили и размером)
zip_file.printdir()
# Переменная с именем файла
file_name = ''
# .namelist() - возвращает имена файлов.
for filename in zip_file.namelist():
    # Разархивирует файл по имени.
    zip_file.extract(filename)
    file_name = filename
zip_file.close()

# Статистика будет храниться в словаре, где ключ это буква, а объект - другой словарь,
# в котором ключи это буквы идущие после первой ключа, а объекты - количество таких случаев.
stat = {}
# stat = {'а': {'т': 500, 'x': 5, }, 'т': {'о': 100, 'у': 50, }, } - пример словаря
# Переменная для предыдущего символа.

analise_count = 4
sequence = ' ' * analise_count
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        line = line[:-1]
        for char in line:
            if sequence in stat:
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence[1:] + char

# pprint.pp(stat)
# pprint.pp(len(stat))
# print('\n', '*' * 27)
#
totals = {}
stat_for_generate = {}
for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, count in char_stat.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    stat_for_generate[sequence].sort(reverse=True)

# pprint.pp(totals)
# pprint.pp(stat_for_generate)

N = 1000
printed = 0

sequence = ' ' * analise_count
spaces_printed = 0
while printed < N:
    char_stat = stat_for_generate[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    if char == ' ':
        spaces_printed += 1
        if spaces_printed >= 10:
            print()
            spaces_printed = 0
    sequence = sequence[1:] + char
    printed += 1
