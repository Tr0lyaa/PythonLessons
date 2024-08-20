import requests
import numpy as np
#
# Requests
#
r = requests.get('https://google.com/')
print(r)
print(r.status_code)
print(r.status_code == requests.codes.ok)
#
# Numpy
#
array_1 = np.array([4, 2, 3])
array_2 = np.array([[3, 2, 1], [1, 2, 3]])
array_3 = np.arange(1, 10, 3)
print(array_1, array_2, array_3, sep='\n')
array_3 = array_3 + array_1
print(array_3)
array_2 = array_2 ** 2
print(array_2)
