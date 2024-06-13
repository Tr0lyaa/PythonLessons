# Методы типа __название__ - это специальные или магические методы классов.
# Их огромное множество, их можно посмотреть напечав __ в момент создания метода
# или по этой ссылке https://docs.python.org/3/reference/datamodel.html#basic-customization.
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Деструктор срабатывает как только исчезают все ссылки на объект или при завершении работы программы.
    def __del__(self):
        print(f'{self.name} ушёл')
# Функция длины может быть переназначина для класса.
    def __len__(self):
        return self.age
# Это работает для большинства встроенных функций.
# __repr__ Работает почти как str, но с какими-то сложными особенностями. Он вызывается в случаях,
# где явно или нет объект преобразовывается в строку.
    def __repr__(self):
        return 'Имя - ' + self.name + ', возраст - ' + str(self.age)

    def __int__(self):
        return self.age


den = Human('Денис', 24)
max = Human('Макс', 23)

del den
print(f'Возраст Макса - {len(max)}')
print(str(max))
print(int(max))
