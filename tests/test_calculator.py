import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calculator = Calculator()
        result = calculator.add(10, 20)
        self.assertEqual(result, 30)

if __name__ == '__main__':
    unittest.main()
