from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power, enemy_count=100):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy_count = enemy_count
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy_count > 0:
            self.days += 1
            self.enemy_count = self.enemy_count - self.power if self.enemy_count >= self.power else 0
            print(f'{self.name}, сражается {self.days} дней(дня), осталось {self.enemy_count}')
            sleep(1)
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
