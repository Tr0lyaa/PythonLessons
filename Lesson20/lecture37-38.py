# Создание класса начинается - class НазваниеКласса:
class Human:
# Инициализатор класса - __init__(self):
# Как и с обычной функцией можно задавать параметры.
# self - это указатель на самого себя (объект).
    def __init__(self, name, age):
# Атрибуты или свойства(характеристики) класса
        self.name = name
        self.age = age
# В инициализаторе можно указывать другие методы. Тогда они будут срабатывать при инициализации переменной.
        self.say_info()
# Всё с def - это методы класса.
# Работотают почти как функции. Методов может быть огромное количество и они работают для каждого объекта класса.
    def birthday(self):
        self.age += 1
        print('У меня день рождения, теперь мне', self.age)

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')
# И методы и атрибуты используются как ссылка на метод(атрибут) класса -> имя_объекта.метод() или имя_объекта.атрибут

# den и max - экземпляры класса или объекты класса.
# Можно создавать (почти) неограниченное количество объектов класса.
den = Human('Денис', 23)
max = Human('Денис', 23)
ann = Human('Анна', 22)

# type() определяет тип как класс созданный в main.
print('Тип den:',type(den))
# Каждый объект или экземпляр уникален.
print('Равен ли den и max:',den == max)
print('den это max:', den is max)
# Находятся в разных ячейках памяти.
print(f'Ячейка памяти den: {id(den)}, ячейка памяти max: {id(max)}')
# Обращение к атрибуту объекта и изменение этого атрибута.
max.name = ('Макс')
print(f'Имя den: {den.name}, возраст den: {den.age}')
print(f'Имя den: {den.name}, имя max: {max.name}')
# Для каждого объекта можно создавать новые атрибуту, которые будут существовать только у этого конкретного объекта.
den.surname = 'Попов'
print('Фамилия den:', den.surname)
# При попытке посмотреть этот атрибут у других объектов этого класса будет ошибка.
# print(max.surname) -> AttributeError: 'Human' object has no attribute 'surname'
# Вызов метода класса для объекта этого класса.
print('Возраст den:', den.age)
den.birthday()
print('Возраст den после дня рождения:', den.age)
max.say_info()
