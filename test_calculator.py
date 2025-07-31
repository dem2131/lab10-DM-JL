#https://github.com/dem2131/lab10-DM-JL.git
# Partner 1: David Miller
# Partner 2: Jacob Lindland

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5, "should return 5")
        self.assertEqual(add(100, 5), 105, "should return 105")
        self.assertEqual(add(4, 4), 8, "should return 8")

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 3), -1, "should return -1")
        self.assertEqual(subtract(10, 5), 5, "should return 505")
        self.assertEqual(subtract(40, 4), 36, "should return 36")


        #more assertions as advised by Ahmed
        self.assertEqual(subtract(13, 7), 6, "should return 6")
        self.assertEqual(subtract(55, 27), 28, "should return 28")
        self.assertEqual(subtract(44, 8), 36, "should return 36")
    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5, 3), 15)
        self.assertEqual(mul(-2, 4), -8)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self): # 3 assertions

        self.assertAlmostEqual(div(2, 10), 5.0)
        self.assertAlmostEqual(div(4, -8), -2.0)
        self.assertAlmostEqual(div(4, 2), 0.5)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):   # 3 assertions
        self.assertEqual(logarithm(5, 25), 2, "should equal 2")
        self.assertEqual(logarithm(10, 100), 2, "should equal 2")
        self.assertEqual(logarithm(2, 256), 8, "should equal 8")
        #more assertions as advised by Ahmed
        self.assertEqual(logarithm(3, 27), 3, "should equal 3")
        self.assertEqual(logarithm(7, 49), 2, "should equal 2")
        self.assertEqual(logarithm(6, 36), 2, "should equal 2")
    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(1, 5)
        with self.assertRaises(ValueError):
            logarithm(5, 0)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-8, 15), 17.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2), 1.41421356)

# Do not touch this
if __name__ == "__main__":
    unittest.main()