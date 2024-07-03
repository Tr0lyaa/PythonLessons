from pprint import pprint

name = 'sample2.txt'
file = open(name, 'r+')  # r, w, a -> r - read, w - write, a - append.

print(file.tell())
pprint(file.read())
print(file.tell())
# Можно перемещать индекс дальше существующего индекса в файле, потому что индекс считает побайтово.
# Из-за этого нужно очень осторожно двигать индексы.
file.seek(16)
file.write('new text')
print(file.tell())
pprint(file.read())
file.close()
# Русских символов нет в ASCII, и нет в кодировке cp1252, поэтому надо брать кодировку utf-8.
name = 'sample.txt'
file = open(name, 'r', encoding='utf-8')
print(file.tell())
pprint(file.read())
print(file.tell())
# Методы, показывающие доступен ли файл для записи, чтения и поиска индексов.
print(file.writable())
print(file.readable())
print(file.seekable())
# Можно выводить атрибуты файла.
print(file.name, file.buffer, file.closed)

file.close()
