import unittest
from src import exponential

class TestExpo(unittest.TestCase):

    def test_power(self):
        self.assertEqual(exponential.power(2, 3), 8)
        self.assertEqual(exponential.power(2, 2), 4)
        self.assertEqual(exponential.power(2, 5), 32)

    def test_power_zero(self):
        self.assertEqual(exponential.power_zero(3), 1)
        self.assertEqual(exponential.power_zero(87), 1)
        self.assertEqual(exponential.power_zero(5), 1)

    def test_power_one(self):
        self.assertEqual(exponential.power_one(100), 100)
        self.assertEqual(exponential.power_one(2), 2)
        self.assertEqual(exponential.power_one(55), 55)

        self.assertRaises(ValueError, exponential.power_one, 0)

    def test_add_two_powers(self):
        self.assertEqual(exponential.add_two_powers(2, 2, 3), 32)
        self.assertEqual(exponential.add_two_powers(3, 2, 1), 27)
        self.assertEqual(exponential.add_two_powers(4, 1, 0), 4)

    # def test_minus_power(self):
    #     self.assertTrue(exponential.minus_power())

if __name__ == '__main__':
    unittest.main()