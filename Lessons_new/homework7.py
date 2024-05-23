my_dict = {'Ann': 1996, 'Kate': 1998, 'Daria': 1997}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict['Ann']}')
print(f'Not existing value: {my_dict.get('Katya')}')
print(f'Deleted value: {my_dict.pop('Kate')}')
my_dict.update({'Alina': 1995, 'Ellina': 1996})
print(f'Modified dictionary: {my_dict}', end='\n\n')

my_set = {1, 2, 1, 1, 'Python', 'Python', 'Hello', 'World'}
print(my_set)
my_set.add(3)
my_set.update({'!!!', 123})
my_set.remove(1)
print(my_set)
