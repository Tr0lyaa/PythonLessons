class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def  go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
            print()
        else:
            print('Такого этажа не существует!', end='\n\n')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(20)
h1.go_to(1)
h1.go_to(15)
h2.go_to(-1)
h2.go_to(2)
