import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5, "should return 5")
        self.assertEqual(add(100, 5), 105, "should return 105")
        self.assertEqual(add(4, 4), 8, "should return 8")

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(2, 3), -1, "should return -1")
        self.assertEqual(sub(10, 5), 5, "should return 505")
        self.assertEqual(sub(40, 4), 36, "should return 36")

    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):   # 3 assertions
        self.assertEqual(log(5, 25), 2, "should equal 2")
        self.assertEqual(log(10, 100), 2, "should equal 2")
        self.assertEqual(log(2, 256), 8, "should equal 8")

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)
        with self.assertRaises(ValueError):
            log(1, 5)
        with self.assertRaises(ValueError):
            log(5, 0)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()