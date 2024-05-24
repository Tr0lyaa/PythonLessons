def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(10,100)
print_params(111, 'тоже строка', False)
# print_params('хэй', 123, 'хэй хэй', True) ->
# TypeError: print_params() takes from 0 to 3 positional arguments but 4 were given
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['точно строка', 11, 12.34]
values_dict = {'a': 89999999999, 'b': '89999999998', 'c': False}

# print_params(values_list) -> ['точно строка', 11, 12.34] строка True
print_params(*values_list)
# print_params(values_dict) -> {'a': 89999999999, 'b': '89999999998', 'c': False} строка True
# print_params(*values_dict) -> a b c
print_params(**values_dict)

values_list_2 = ['строчка', 89.0]
print_params(*values_list_2, 42)
