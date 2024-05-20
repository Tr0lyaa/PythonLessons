import random
def print_params(arg):
    print(arg, arg, sep='\n', end='\n\n')

args_list = [1, 2, 10, 123, 'hello', 'world', [1, 2, 3]]
arg = random.choice(args_list)

print_params(arg)
print_params(arg)
print_params(arg)
