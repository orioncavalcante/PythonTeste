import unittest

class MathOperations:
    def multiply(self, a, b):
        return a * b

class TestMathOperations(unittest.TestCase):
    def test_multiply(self):
        math = MathOperations()
        self.assertEqual(math.multiply(3, 4), 12)
        self.assertEqual(math.multiply(-1, 5), -5)

if __name__ == "__main__":
    unittest.main()
