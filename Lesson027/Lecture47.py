# Множественное наследование.
# Мы может наследовать множество классов. Для этого мы записываем их в дочернем классе через запятую.
# У всех классов есть иерархия наследования. Её можно посмотреть с помощью команды имяКласса.mro().
# Иерархия работает слево направо. У всех классов есть наследуемый класс object (встроенный класс пайтона).
# То есть сначала мы смотрим на всё в самом классе, потом в классе указаном справа и т.д.
class Human:
    def __init__(self, name, group):
        self.name = name
        # Этот super будет обращаться к второму родительскому классу Student при вызове.
        super().__init__(group)
        super().about()

    def info(self):
        print(f'Привет, меня зовут {self.name}')

class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')
class Student(Human, StudentGroup):
    def __init__(self,name, place, group):
        # Метод super() обращается к родительскому классу.
        super().__init__(name, group)
        self.place = place
        super().info()


print(Student.mro())
student = Student('Макс', 'Урбан', 'Пайтон 1')
# При этом класс Student также унаследовал все методы родительских классов.
student.about()
student.info()
