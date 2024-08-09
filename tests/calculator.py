import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        result = calculator.add(10, 20)
        self.assertEqual(result, 30)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(2, 2)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()