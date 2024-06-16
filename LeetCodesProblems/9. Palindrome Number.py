# Класс Solution используется как шаблон на Leetcode.
# Задача: Дано целое число, вывести true, если это число палиндром, в обратном случае вывести false.
class Solution:
    def isPalindrome(self, x):
        # Если число отрицательное или заканчивается на 0 то оно точно не палиндром.
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        # В переменной x_reversed будет поразрядно собираться число в обратном порядке.
        x_reversed = 0
        # Цикл доходит до приблизительно середины числа, так как нет смысла переворачивать всё число, а только его половину.
        while x > x_reversed:
            x_reversed = x_reversed * 10 + x % 10
            x = x // 10
        # Сравниваем полученные числа (если число разрядов нечётное то сравниваем x с x_reversed // 10)
        return True if (x == x_reversed or x == x_reversed // 10) else False

num = Solution()
print(num.isPalindrome(12121))
