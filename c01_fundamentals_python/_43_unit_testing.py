"""
TEST UNITARIOS

Are units of code that test every part in a program. The unit testing
process:

- Identify the unit
- Define the test case
- Write test code
- Execute the tests
- Debug and iterate

THe beauty of unit testing lies in its ability to detext problems early
in the development process.

Rigorously testing each unit allows you to identify and fix these problems
before they can cause widespread damage.
"""
import pytest


def calculateDiscount(price, discount):
    return price - (price * discount / 100)


class TestDiscountCalculation:

    def testTenPercentDiscount(self):
        result = calculateDiscount(price=100, discount=10)
        assert result == 90

    def testInvalidInput(self):
        with pytest.raises(TypeError):
            calculateDiscount("100", 10)
