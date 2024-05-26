def get_multiplied_digits(number):
    first = int(number[0])
    if len(number) == 1:
        if first == 0:
#            print(first)
            return 1
        else:
#            print(first)
            return first
    else:
#        print(first, '*', number[1:])
        if number[0] == '0':
            return get_multiplied_digits(number[1:])
        return first * get_multiplied_digits(number[1:])

while True:
    str_number = input('Введите целое число или введите 0 для прекращения: ')

    if not str_number.isdigit():
        print('Ошибка ввода')
        continue
    if int(str_number) == 0:
        print('Число равно 0')
        break
    print(get_multiplied_digits(str_number))
