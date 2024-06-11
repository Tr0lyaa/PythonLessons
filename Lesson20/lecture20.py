class Toyota:

    def __init__(self):
        self.color = "Бордовый металик"
        self.price = "1000000 рублей"
        self.max_velocity = "200 км/ч"
        self.current_velocity = "0 км/ч"
        self.engine_rpm = 0

    def start(self):
        print('Мотор запущен!')
        self.engine_rpm = 900

    def go(self):
        print('Поехали!')
        self.engine_rpm = 2000
        self.current_velocity = "20 км/ч"

my_car = Toyota()

print('Color:', my_car.color)
print('Price:', my_car.price)
print('Max velocity:', my_car.max_velocity)
print('Current rpm:', my_car.engine_rpm)
print('Current velocity:', my_car.current_velocity, end='\n\n')

my_car.start()
print('Current rpm:', my_car.engine_rpm)
my_car.go()
print('Current rpm:', my_car.engine_rpm)
print('Current velocity:', my_car.current_velocity, end='\n\n')


produced, plan = 0, 10
stock = []
while produced < plan:
    new_car = Toyota()
    stock.append(new_car)
    produced = len(stock)

print("Произведено: ", produced)
print("План: ", plan)
print(stock, end='\n\n')


class Robot:

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print('Привет, мир! Я - ', self.name)

robot = Robot()
robot.hello()

some_var = robot
some_var.hello()

some_robot = some_var
some_robot.hello()

some_robot.name = 'C-3PO'
some_robot.hello()
some_var.hello()
robot.hello()

some_another_robot = Robot()
some_another_robot.hello()