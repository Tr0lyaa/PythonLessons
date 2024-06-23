# Испоользование нижнего подчёрккивания в пайтон.
# В интерактивном режиме _ сохраняет последний результат:
# 5 + 5 -> 10 10
# + _ -> 20
# _ + _ -> 40
# При использовании в названии делает переменную, класс, функцию (и так далее)
# доступными только в локальном пространстве имён и всем пространствам ниже уровнем.
# Двойное подчёркивание защищает имя от переназначение (переопределения) в дочерних классах.
class Human:
    head = True
    _legs = True
    __arms = True

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)

    def say_hello(self):
        print('Здраствуйте')

class Student(Human):
    pass

class Teacher(Human):
    pass


human = Human()
human.about()

student = Student()
student.about()

print(dir(human))
print(dir(student))
# Мы можем получить доступ к этому атрибуту через _имяКласса_.__названиеАтрибута, а также через методы класса,
# но не можем напрямую через дочерний класс.
print(student._Human__arms)
# print(student.__arms) -> 'Student' object has no attribute '__arms'
# При этом к локальным атрибутам мы можем обратиться и через дочерний класс,
# так как его пространство имён находится ниже или глубже родительского.
print(student._legs)
