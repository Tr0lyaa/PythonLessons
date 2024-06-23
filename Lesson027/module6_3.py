class Vehicle:
    vehicle_type = None

class Car:
    price = 1000000

    def horse_powers(self):
        print('Я из класса Car, мощность двигателя:', end=' ')
        return self.power

    def engine_powers(self):
        print('Я из класса Car, мощность двигателя:', end=' ')
        return self.power

class Nissan(Vehicle, Car):
    power = 500

    def __init__(self, vehicle_type, price):
        self.vehicle_type = vehicle_type
        self.price = price

    def horse_powers(self):
        print('Я из класса Nissan, мощность двигателя:', end=' ')
        return self.power


car1 = Nissan('Car', '1200000')
print(car1.vehicle_type, car1.price)
print(car1.horse_powers())
print(car1.engine_powers())
