# Класс Solution используется как шаблон на Leetcode.
# Задача: Дана строка s, нужно найти максимальную длину подстроки, в которой нет повторяющихся элементов.
# Например: "aabaab!bb" - строка, "ab!" - максимально длинная подстрока без повторений.
class Solution:
    def lengthOfLongestSubstring(self, s):
        # Создаём пустую строку, куда будут записываться элементы.
        sub_str = ''
        # Сохраняем максимальную длину. Изначально равно 0, чтобы точно перезаписаться.
        max_length = 0
        # По штучно проверяем есть ли такой элемент в подстроке, если нет то добавляем в подстроку.
        # Иначе записываем новую максимальную длину, если она больше уже записанной.
        for char in s:
            if char not in sub_str:
                sub_str += char
            else:
                max_length = len(sub_str) if max_length < len(sub_str) else max_length
                # Потом добавляем текущий элемент к подстроке.
                sub_str += char
                # Создаём новую подстроку из старой.
                # С помощью поиска находим индекс элемента, который совпадает с текущим и
                # создаём подстроку, начиная со следующего индекса.
                sub_str = sub_str[sub_str.find(char)+1:]
        return len(sub_str) if len(sub_str) > max_length else max_length

s = Solution()

print(s.lengthOfLongestSubstring("aabaab!bb"))
