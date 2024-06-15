# Перегрузка - переназначение уже существующих функций, методов для своих классов.
class House:
    def __init__(self, building, numberOfFloors, age):
        self.building = building
        self.numberOfFloors = numberOfFloors
        self.age = age
    # __lt__ - оператор меньше.
    def __lt__(self, other):
        return self.numberOfFloors < other.numberOfFloors
    # __gt__ - оператор больше.
    def __gt__(self, other):
        return self.numberOfFloors > other.numberOfFloors
    # __eq__ - оператор равенства.
    def __eq__(self, other):
        return self.building == other.building and self.numberOfFloors == other.numberOfFloors
    # __bool__ - значения истинности (скорее относится к "магическим" методам).
    def __bool__(self):
        return bool(self.age)
    # __str__ - строковое представление объекта.
    def __str__(self):
        return f'Это здание: {self.building}, этажей: {self.numberOfFloors}, возраст в годах: {self.age}'


house1 = House("Высотка", 20, 15)
house2 = House("Пятиэтажка", 5, 50)
house3 = House("Пятиэтажка", 5, 65)

print(house1 < house2)
print(house1 > house2)
print(house1 == house2)
print(house3 == house2)
print(house3)
