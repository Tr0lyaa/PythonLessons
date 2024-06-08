from random import randint
from termcolor import cprint, colored

MAX_BUNCHES = 10
MAX_BUNCHES_SIZE = 20
_holder = {}

def put_stones():
    global _holder
    _holder = {}
    while True:
        bunches = input(colored(f'Введите число куч от 3 до {MAX_BUNCHES}: ', color = 'green', force_color='True'))
        if bunches.isdigit() and 3 <= int(bunches) <= MAX_BUNCHES:
            for i in range(1, int(bunches) + 1):
                _holder[i] = randint(1, 20)
            break
        else:
            cprint('Ошибка ввода!', 'red', force_color='True')

def check_pos(pos):
    if pos.isdigit() and int(pos) in _holder and _holder[int(pos)] >= 1:
        return True
    else:
        cprint('Ошибка ввода!', 'red', force_color='True')
        return False

def check_qua(pos, qua):
    if qua.isdigit() and 1 <= int(qua) <= _holder[int(pos)]:
        return True
    else:
        cprint('Ошибка ввода!', 'red', force_color='True')
        return False

def take_from_bunch(position, quantity):
    if position in _holder:
        _holder[position] -= quantity

def get_bunches():
    res = []
    for key in sorted((_holder.keys())):
        res.append(_holder[key])
    return res

def is_gameover():
    return sum(_holder.values()) == 0
