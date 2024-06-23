# Реализуем модель доставки грузов

# Дорога - хранит расстояния между обьектами
# Склад - хранит груз и управляет очередями грузовиков

# Базовый класс - Машина,
# имеет
#   кол-во топлива
# может
#   заправляться

# Грузовик (производный от Машина)
# имеет
#   емкость кузова, скорость движения, расход топлива за час поездки
# может
#   стоят под погрузкой/разгрузкой
#   ехать со скоростью

# Погрузчик (производный от Машина)
# имеет
#   скорость погрузки, расход топлива в час при работе
# может
#   загружать/разгружать грузовик
#   ждать грузовик
#
# Всю работу грузовиков и погрузчиков разделим по часам
# и будем каждый час проверять и обновлять данные по ведущимся работам

from random import randint
from termcolor import cprint

class Road:

    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:

    def __init__(self, name, content = 0):
        self.name = name
        self.content = content
        self.set_road_out = None

    def __str__(self):
        return f'Склад {self.name} груза {self.content}'

    def set_road_out(self, road):
        self.set_road_out = road

    def truck_arrived(self, truck):
        pass

    def get_next_truck(self):
        pass

    def truck_ready(self, truck):
        pass

    def act(self):
        pass


class Vehicle:
    fuel_rate = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return f'{self.model}, топлива {self.fuel}'

    def tank_up(self):
        self.fuel += 1000


class Truck(Vehicle):

    def __init__(self, model, body_space = 1000):
        super().__init__(model=model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0

    def __str__(self):
        return f'{super().__str__()}, текущий груз {self.cargo} кг'

    def ride(self):
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
        print(f'{self.model} едет по дороге, осталось {self.distance_to_target}')

    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance
        print(f'{self.model} выехал в путь')

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
        elif isinstance(self.place, Road):
            self.ride()


class AutoLoader(Vehicle):

    def __init__(self, model, bucket_capacity = 100, warehouse = None, role = 'loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        return f'{super().__str__()}, груза {self.truck}'

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
        elif self.truck is None:
            self.truck = self.warehouse.get_next_truck()
        elif self.role == 'loader':
            self.load
        else:
            self.unload()

    def load(self):
        truck_cargo_rest = self.truck.body_space - self.truck.cargo
        if truck_cargo_rest >= self.bucket_capacity:
            self.warehouse.content -= self.bucket_capacity
            self.truck.cargo += self.bucket_capacity
        else:
            self.warehouse.content -= truck_cargo_rest
            self.truck.cargo += truck_cargo_rest

    def unload(self):
        if self.truck.cargo >= self.bucket_capacity:
            self.warehouse.content += self.bucket_capacity
            self.truck.cargo -= self.bucket_capacity
        else:
            self.warehouse.content += self.truck.cargo
            self.truck.cargo = 0


TOTAL_CARGO = 100000

moscow = Warehouse(name='Москва', content=TOTAL_CARGO)
piter = Warehouse(name='Питер', content=0)

moscow_piter = Road(start=moscow, end=piter, distance=715)
piter_moscow = Road(start=piter, end=moscow, distance=780)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = AutoLoader(model='Bobcat', bucket_capacity=1000, warehouse=moscow, role='loader')
loader_2 = AutoLoader(model='Lonking', bucket_capacity=500, warehouse=piter, role='unloader')

truck_1 = Truck(model='КАМАЗ', body_space=5000)
truck_2 = Truck(model='ГАЗ', body_space=2000)

moscow.truck_arrived(truck_1)
moscow.truck_arrived(truck_2)

hour = 0

while piter.content < TOTAL_CARGO:
    hour += 1
    cprint(f'-----{hour}-----', color='red')
    truck_1.act()
    truck_2.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    cprint(truck_1, color='cyan')
    cprint(truck_2, color='cyan')
    cprint(loader_1, color='cyan')
    cprint(loader_2, color='cyan')
    cprint(moscow, color='cyan')
    cprint(piter, color='cyan')
