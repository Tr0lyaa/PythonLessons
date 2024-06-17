# Класс Solution используется как шаблон на Leetcode.
# Задача: Дана строка s, нужно найти максимальную длину подстроки, которая является палиндромом.
# Например: "aabaab!bb" - строка, "aabaa" - максимально длинная подстрока-палиндром.
class Solution:
    def longestPalindrome(self, s):
        # Создаём вспомогательный метод expand.
        # Он измеряет границы палиндрома, начиная из центра.
        def expand(i, j):
            left = i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Возращаем длину палиндрома.
            return right - left - 1
        # Индексы границ самого длинного палиндрома.
        coordinates = [0, 0]

        for i in range(len(s)):
            # Считаем палиндром с нечётным количеством символов.
            # Если такой находится, то проверяем с длиной сохранённой в ans[].
            odd_length = expand(i, i)
            if odd_length > coordinates[1] - coordinates[0] + 1:
                # Записываем новые координаты с помощью dist и текущего i (центра).
                # Для нечётного палиндрома он будет половиной полученной длины.
                dist = odd_length // 2
                coordinates = [i - dist, i + dist]
            # Для чётного палиндрома центр состоит из двух элементов i и i + 1.
            even_length = expand(i, i + 1)
            if even_length > coordinates[1] - coordinates[0] + 1:
                # При прохождении проверки также записываем новые координаты,
                # но теперь расстояния от центра будет уменьшаться на 1 из-за двойного центра.
                dist = (even_length // 2) - 1
                coordinates = [i - dist, i + 1 + dist]
        # И так для каждого элемента проверяется центр ли он палиндрома (нечётного и чётного).

        i, j = coordinates
        return s[i : j + 1]

s = Solution()
print(s.longestPalindrome("aabaab!bb"))
