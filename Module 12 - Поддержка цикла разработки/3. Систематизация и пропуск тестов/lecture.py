import unittest
import test_calc

# Создание тест сьюта (сборника тестов).
calcST = unittest.TestSuite()
# Добавление тестов в сборник.
# Это старый метод и он перестанет работать в python 3.13!
# calcST.addTest(unittest.makeSuite(test_calc.CalcTest))
# Это новый метод.
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calc.CalcTest))
# Для запуска тестов используем runner.
# У него есть параметр verbosity - это детализация тестов
runner = unittest.TextTestRunner(verbosity=2)
# runner.run(название_тест_сьюта) - запуск runner с необходимым сборником тестов.
runner.run(calcST)
