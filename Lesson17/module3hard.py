def calculate_structure_sum(*args, **kwargs):
    sum = 0

    if isinstance(args[0], dict):
        for i in args[0].keys():
            sum += len(i) + args[0][i]
        return sum

    for i in args[0]:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, dict) or isinstance(i, set):
            sum += calculate_structure_sum(i)
        elif isinstance(i, int) or isinstance(i, float):
            sum += i
        else:
            sum += len(i)
    return sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
