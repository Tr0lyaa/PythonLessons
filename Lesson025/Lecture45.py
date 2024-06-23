# Наследование - передача атрибутов, методов и т.д. от родительского класса к дочернему классу.
# Класс Human будет являться родительским классом и передавать свой классовый атрибут в класс Student.
class Human:
    head = True
    chest = True

    def __init__(self):
        self.about()

    def say_hello(self):
        print('Здраствуйте')

# Класс Student является дочерним классом.
# Для этого необходимо после названия класса написать в круглых скобках название другого класса.
class Student(Human):
    # Если названия атрибутов в разных классах совпадают, то вызывается атрибут дочернего класса.
    chest = False

    def about(self):
        print('Я студент')

# Одиннаковые методы можно вынести в родительский класс для избежания повторений.
#    def say_hello(self):
#        print('Здраствуйте')

class Teacher(Human):

    def about(self):
        print('Я преподаватель')

#    def say_hello(self):
#        print('Здраствуйте')


# Из-за вызова self.about нельзя просто создать экземпляр класса Human.
# human = Human() -> Создание экземпляра класса Human.
student = Student()
teacher = Teacher()

# print(human.head) -> True, но с about нельзя использовать просто экземпляр класса Human.
# print(human.chest) -> True.
student.about()
print(student.head)
print(student.chest)
# Только дочерний класс получает доступ к пространству имён из родительского, в обратную сторону это не работает.
# print(student.head) -> True
# human.about() -> AttributeError: 'Human' object has no attribute 'about'

teacher.say_hello()
student.say_hello()
