import os
import time
# Для пути в Windows необходимо писать два обратных слеша(экранировать слеш) между директориями.
# Для работы с файлами на уровне ОС есть три встроенных модуля: os, os.path, shutil.
path = 'C:\\Windows\\help'
path2 = 'C:/Windows/help'
path2 = os.path.normpath(path2)
file_name = 'test.txt'
print(path2)

# Пройтись по всем файлам в директории.
count = 0
for dirpath, dirnames, filenames in os.walk(path):
    print('*' * 27)
    print(dirpath, dirnames, filenames)
    print(os.path.dirname(dirpath))
    count += len(filenames)
    for file in filenames:
        # Для работы с фалами нужен полный путь к ним.
        # Его можно получить из dirpath (путь к директории) + '\\' (для перехода внутрь) + file (имя файла).
        # Например: full_name_path = dirpath + '\\' + file
        # Или с помощью метода. Этот вариант лучше, потому что он создаёт путь с учётом текущей ОС.
        full_name_path = os.path.join(dirpath, file)
        secs = os.path.getmtime(full_name_path)
        file_time = time.gmtime(secs)
        if file_time[0] == 2022:
            print(full_name_path, secs)
        else:
            print(full_name_path, secs, file_time[0])

print(count)
print(__file__, os.path.dirname(__file__))

# Эта команда приводит путь к типизованному для этой ОС пути.
os.path.normpath(path)
# Эта команда возвращает размер файла.
os.path.getsize(path)
# Возвращает количество секунд с модификации файла.
os.path.getmtime(path)
# Преобразует полученные секунды в дату и время.
time.gmtime(10)
# Возвращает полный путь до файла.
os.path.join(path, file_name)
# Возвращает родительскую директорию.
os.path.dirname(path)
# Возвращает родительскую директорию текущего модуля.
os.path.dirname(__file__)
