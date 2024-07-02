# Кодировки символов и байты.

print('Hello')  # таблица ASCII - 128 символов.
# ord - команда для вывода ASCII номера для символов.
print(ord('a'))

chars = []
_str = 'hello'
for i in _str:
    chars.append(ord(i))
print(chars)

s = ''
for i in chars:
    s += chr(i)

print(s)

for i in range(128):
    print(chr(i), end=' ')
print()
# В Пайтоне используется Unicode таблица, там практически все символы.
for i in range(1000, 1200):
    print(chr(i), end=' ')
print()

# hex - переводит код символа в шестнадцатеричный вид.
print(hex(ord('h')))
# b'текст' - байтовый тип данных.
bb = b'\x68'
print(type(bb))
print(bb.decode())
