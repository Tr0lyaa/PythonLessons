from random import randint
from termcolor import colored

MAX_BUNCHES = 5
_holder = []

def put_stones():
    global _holder
    _holder = []
    bunches = input(colored(f'Введите число куч от 1 до {MAX_BUNCHES}: ', color = 'green', force_color='True'))

    for i in range(int(bunches)):
        _holder.append(randint(1, 20))


def take_from_bunch(position, quantity):
    if 1 <= position <= len(_holder):
        _holder[position - 1] -= quantity


def get_bunches():
    return _holder


def is_gameover():
    return sum(_holder) == 0
