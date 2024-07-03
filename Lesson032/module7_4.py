team1_num = 6
team2_num = 6
print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %(team1)s и %(team2)s!' % {'team1': team1_num, 'team2': team2_num})

score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {time} с!'.format(time=team2_time))

print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_2 > score_1 or score_2 == score_1 and team2_time > team1_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья'
print(f'Результат битвы: {challenge_result}')
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 1)
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {time_avg} секунды на задачу!')
