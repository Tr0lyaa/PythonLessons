# Однонаправленный список - список, в котором хранится элемент и следующий элемент списка.
# Из-за этого в таких списках нет индексации и только некий указатель на элементы списка.
# val - текущий элемент, следующий элемент - next.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Метод для вывода содержимого списка.
    def print_numbers(self):
        # Пока текущий элемент списка не None.
        while self != None:
            # Выводим элемент списка. Убираем перевод на следующую строку для удобства.
            print(self.val, end='')
            # Перемещаем указатель на следующий элемент списка.
            self = self.next
        # Пустой вывод для удобства чтения.
        print()

    def create_list(self):
        number = input("Введите своё число: ")
        number = number[::-1]
        result = ListNode(0)
        current = result
        for i in number:
            current.next = ListNode(int(i))
            current = current.next

            number = number[1:]

        return result.next

# Класс Solution используется как шаблон на Leetcode.
# Задача: Даны два непустых связных списка, представляющие два неотрицательных числа.
# Цифры хранятся в обратном порядке, и каждый их узел содержит одну цифру.
# Сложите два числа и верните сумму в виде связного списка.
# Можно предположить, что оба числа не содержат начальных нулей, кроме самого числа 0.
class Solution:
    # Считаем сумму чисел записанных в двух однонаправленных списках в обратном порядке.
    def addTwoNumbers(self, l1, l2):
        # Создаём результирующий список и записываем в него None.
        result = ListNode(None)
        # Создаём указатель, который будет перемещаться по нашему результирующему списку.
        # Без него будет потерян первый элемент списка, а в однонаправленных списках снова найти его невозможно.
        current = result
        # carry - это остаток, который переносится в следующий разряд.
        # Например: 6 + 7 = 13 -> 1 уходит в следующий разряд, а 3 остаётся в этом.
        carry = 0
        # Пока в наших списках есть числа (то есть они не равны None) и остаток не равен 0.
        while l1 != None or l2 != None or carry != 0:
            # Если текущие значения в списках не равны None, то мы их записываем, иначе записываем 0.
            # Это нужно на случай если списки (то есть числа) разной длины.
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            # Считаем сумму текущего разряда (первая цифра первого списка + первая цифра второго списка + остаток).
            element_sum = l1_val + l2_val + carry
            # Записываем новый остаток (сумму разряда делим на 10 и берём целую часть).
            carry = element_sum // 10
            # Заменяем первый элемент результирующего списка.
            # И записываем следующие элементы списков. Если они не None, то записываем оставшуюся часть, иначе None.
            # И идём к следующей итерации.
            if result.val == None:
                result.val = element_sum % 10

                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None

                continue
            # Записываем новый результат в следующий элемент результирующего списка.
            # И передвигаем указатель current на следующий элемент в результирующем списке.
            current.next = ListNode(element_sum % 10)
            current = current.next
            # И записываем следующие элементы списков. Если они не None, то записываем оставшуюся часть, иначе None.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # Выводим результирующий список.
        return result
# Создаём два однонаправленных списка.
list1 = ListNode()
# Используем методы для создания и вывода списка. Для проверки работы методов.
list1 = list1.create_list()
list1.print_numbers()
list2 = ListNode()
list2 = list2.create_list()
list2.print_numbers()
# Проверяем решение с помощью класса Solution.
list3 = Solution()
list3 = list3.addTwoNumbers(list1, list2)
list3.print_numbers()
