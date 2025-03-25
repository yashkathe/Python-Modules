#########################################
# Test Files should start with name test #
##########################################

import unittest

import calc


# name of the class should be descriptive
class Test_Calculation(unittest.TestCase):

    # methods should start with test_
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(10, -5), 5)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(10, -5), 15)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(5, -2), -10)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(10, -5), -2)
        self.assertEqual(calc.divide(-1, -1), 1)
        
        # CHECKING FOR EXCEPTIONS

        # METHOD 1
        # we do it this way
        # because if we run the function directly here we will get an error
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # METHOD 2 (recommended)
        # using context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()

#########################################
#                                       #
#        RUNNING THE TEST FILES         #
#                                       #
# ❌ if __name__ == 'main' is not setup #
#                                       #
# python3 -m unittest test_filename.py  #
#                                       #
#  ✅ if __name__ == 'main' is setup    #
#                                       #
#       python3 test_filename.py        #
##########################################


# Notes

# - if we find a test case which still breaks the code despite all the tests
# we should immediately add that test case to our test

# - Tests should be isolated 
# They should not rely on other test or affect other test 
# InShort -> Tests should be independent

# - Test Driven Development
# It means write tests before we write the code
