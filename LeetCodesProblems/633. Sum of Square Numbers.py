# Для метода sqrt для извлечения корня
from math import sqrt
# Класс Solution используется как шаблон на Leetcode.
# Задача: Дано неотрицательное целое число c, определить есть ли такая сумма квадратов чисел a и b равная c
# Пример: c - 2, Ответ: True | 1*1 + 1*1 = 2 | a*a + b*b = c.
class Solution:
    def judgeSquareSum(self, c):
        for first in range((int(sqrt(c))) + 1):
            second = c - first * first

            left = 0
            right = second
            mid = second // 2

            while mid * mid != second and left <= right:

                if second > mid * mid:
                    left = mid + 1
                else:
                    right = mid - 1

                mid = (right + left) // 2

            if right >= left:
                return True

        return False


s = Solution()
print(s.judgeSquareSum(99999999))
