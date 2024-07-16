def is_prime(func):

    def wrapper(first, second, third):
        sum_ = func(first, second, third)
        for i in range(2, sum_):
            if sum_ % i == 0:
                return f'Составное \n{sum_}'
        else:
            return f'Простое \n{sum_}'

    return wrapper


@is_prime
def sum_three(first, second, third):
    return first + second + third


result = sum_three(2, 3, 6)
print(result)
