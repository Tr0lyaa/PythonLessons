name = 'sample.txt'
# Оператор with позволяет создать блок кода, в котором будет существовать указанный объект.
# В случае файлов, их можно не закрывать вручную.
with open(name, encoding='utf-8') as file:
    for line in file:
        for char in line:
            print(char, end='')
    print()
    print(file.tell())
