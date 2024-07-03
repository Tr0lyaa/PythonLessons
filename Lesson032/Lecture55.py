# Форматирование строк.
# Старые методы.
print('Привет, ' + 'мир!')
print('Меня зовут %s, мне %s' % ('Денис', 20))    # %s, %d, %x
print('Меня зовут %(name)s, мне %(year)s' % {'name': 'Денис', 'year': 20})
# Метод format.
print('Я учусь в {}{}'.format('Урбан', '-university'))
print('Я учусь в {0}{1} {0}'.format('Урбан', '-university'))
print('Я учусь в {title}{postfix} {title}'.format(title='Урбан', postfix='-university'))
# Самый новый метод - f-строки. В {} можно вписывать любой питоновский код.
print(f'{'Urban'} это лучший университет')
print(f'{'Urban' * 2} это лучший университет')
