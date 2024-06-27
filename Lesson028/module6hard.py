from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled = False):
        self.__color = list(color)
        self.__sides = []
        if len(sides) != self.sides_count:
            for i in range(self.sides_count):
                self.__sides += 1
        else:
            for i in sides:
                self.__sides.append(i)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print('Некорректный цвет')

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, args):
        for i in args:
            if i <= 0 or self.sides_count != len(args):
                return False

        return True

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = []
            for i in sides:
                self.__sides.append(i)
        else:
            print('Некорректные данные о сторонах')

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled = False):

        super().__init__(color, sides)
        self.__radius = len(self) / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled = False):

        super().__init__(color, sides)
        self.__height = 2 * self.get_square() / self.get_sides()[0]

    def get_square(self):
        sides = self.get_sides()
        p = len(self) / 2
        return sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled = False):

        if len(sides) == 1:
            sides *= 12

        super().__init__(color, sides)
        if len(sides) == 1:
            self.__sides == []
            for i in range(0, 12):
                self.__sides += sides[0]

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10)
triangle1 = Triangle((155, 20, 14),20, 10, 15)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)
print(circle1.get_color())
print(cube1.get_color(), end='\n\n')

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)
print(cube1.get_sides())
print(circle1.get_sides(), end='\n\n')

# Проверка работы len (периметр):
print(len(circle1))
print(len(triangle1))
print(len(cube1), end='\n\n')

# Проверка работы методов дочерних классов:
print(circle1.get_square())
print(triangle1.get_square())
print(cube1.get_volume())
