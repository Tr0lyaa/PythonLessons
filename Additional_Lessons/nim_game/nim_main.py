from nim_engine import get_bunches, put_stones, is_gameover, take_from_bunch, check_pos, check_qua
from termcolor import cprint, colored
import os

os.system('color')
put_stones()
user_number = 1

while True:
    cprint(f'Количество камней в кучах: {get_bunches()}', 'green', force_color='True')

    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint(f'Ход игрока номер {user_number}', user_color, force_color='True')

    while True:
        pos = input(colored('Откуда берём: ', user_color, force_color='True'))
        if check_pos(pos):
            break

    while True:
        qua = input(colored('Сколько берём: ', user_color, force_color='True'))
        if check_qua(pos, qua):
            break

    take_from_bunch(int(pos), int(qua))

    if is_gameover():
        cprint(f'\nВыиграл игрок номер {user_number}! Поздравляем!!!\n', user_color, force_color='True')

        if input(colored('Если хотите сыграть напишите 1: ', 'green', force_color='True')) == '1':
            put_stones()
            user_number = 1
            continue
        else:
            break

    user_number = 2 if user_number == 1 else 1
