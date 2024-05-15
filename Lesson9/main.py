x = 38

print("0 -", 'дратути')
if x < 0:
    print("1 -", 'Меньше нуля')
print("2 -", 'дотвидания')

a, b = 10, 5

if a > b:
    print("3 -", 'a > b')

if a > b and a > 0:
    print("4 -", 'успех')

if (a > b) and (a > 0 or b < 1000):
    print("5 -", 'успех')

if 5 < b and b < 10:
    print("6 -", 'успех')

if '34' > '121':
    print("7 -", 'успех')

if '123' > '12':
    print("8 -", 'успех')

if [1, 2] > [1, 1]:
    print("9 -", 'успех')

# if '6' > 5:
#    print("10 -", 'успех')
# TypeError: '>' not supported between instances of 'str' and 'int'

# if [5, 6] > 5:
#    print("11 -", 'успех')
# TypeError: '>' not supported between instances of 'list' and 'int'

if '6' != 5:
    print("12 -", 'успех')
