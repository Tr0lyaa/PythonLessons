def test():
    a, b = 'print', 100
    print(a, b)

def test2(a, b, c):
    print(a, b, c)

#def test3(a, *, b = 10, c = 'hello'):
#    print(a, b, c)

test()
test2(1, 'world', [1, 2, 3])
#test3(100)
