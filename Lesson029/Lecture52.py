from pprint import pprint

# Для работы нужно полное имя файла.
name = 'sample.txt'
# Файл нужно открыть в определённом режиме.
file = open(name, 'r')  # r, w, a -> r - read, w - write, a - append.
print(file)
# tell - возвращает текущий индекс чтения.
print(file.tell())
pprint(file.read())
# После чтения индекс стал последним, и ещё раз прочитать не получится, пока мы не изменим индекс.
print(file.tell())
pprint(file.read())
# seek - сдвигает текущий индекс на указанный.
print(file.seek(20))
pprint(file.read())
# В конце нужно закрыть файл.
file.close()

name2 = 'sample2.txt'
# При режиме записи весь файл стирается. Если такого файла нет, то он создаётся.
file = open(name2, 'w')
file.write('hello')
file.close()

file = open(name2, 'a')
file.write(', world')
file.close()
