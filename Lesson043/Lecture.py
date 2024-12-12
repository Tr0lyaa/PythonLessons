# Декоратор - функция для функции. Оборачивает функцию в себя, добавляя или меняя её функционал.
def null_decorator(func):
    return func


# Есть два основных способа обернуть в декоратор:
# Это специальный "сахарный" синтаксис - @имя_декоратора перед функцией.
@null_decorator
def greet():
    return 'Hello'


print(greet())
# Второй способ - это "приравнять" (декорировать) функцию с помощью - имя_функции = имя_декоратора(имя_функции).
greet = null_decorator(greet)
print(greet())


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet():
    return 'Hello'


print(greet())
