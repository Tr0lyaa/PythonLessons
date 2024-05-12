immutable_var = (1, "2", [1, 2], True)
print(immutable_var)

immutable_var[2][1] = 3
print(immutable_var, "\n")
# immutable_var[0] = 2
# print(immutable_var)
# TypeError: 'tuple' object does not support item assignment

mutable_list = [1, "2", [1, 2], True]
print(mutable_list)
mutable_list[0] = '2'
mutable_list[1] = 3
mutable_list[3] = False
print(mutable_list)
