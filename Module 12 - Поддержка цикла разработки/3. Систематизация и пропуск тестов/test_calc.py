import calc
import unittest


class CalcTest(unittest.TestCase):
    # Пропуск любого теста с указанием причины.
    @unittest.skip("Не нравится")
    def test_add(self):
        """
        Test for add function in calculator
        :return:
        """
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(2, 5), 10)

    def test_div(self):
        self.assertEqual(calc.div(8, 4), 2)


if __name__ == "__main__":
    unittest.main()
