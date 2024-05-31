from fake_math import divide as divide_fake
from true_math import divide as divide_true

print(divide_fake(100, 20))
print(divide_fake(100, 0))

print(divide_true(20, 5))
print(divide_true(20, 0))
