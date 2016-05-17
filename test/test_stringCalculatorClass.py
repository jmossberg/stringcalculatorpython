import unittest

from src.StringCalculatorClass import StringCalculatorClass


class TestStringCalculatorClass(unittest.TestCase):
    def test_add(self):
        # Setup
        stringCalculatorClass = StringCalculatorClass()

        # Excercise
        result = stringCalculatorClass.add("")

        # Verify
        assert 0 == result

    def test_add1(self):
        # Setup
        stringCalculatorClass = StringCalculatorClass()

        # Excercise
        result = stringCalculatorClass.add("1")

        # Verify
        assert 1 == result


    def test_add2(self):
        # Setup
        stringCalculatorClass = StringCalculatorClass()

        # Excercise
        result = stringCalculatorClass.add("2")

        # Verify
        assert 2 == result


    def test_add1and2(self):
        # Setup
        stringCalculatorClass = StringCalculatorClass()

        # Excercise
        result = stringCalculatorClass.add("1,2")

        # Verify
        assert 3 == result


    def test_add5numbers(self):
        # Setup
        stringCalculatorClass = StringCalculatorClass()

        # Excercise
        result = stringCalculatorClass.add("1,2,17,4,1,1")

        # Verify
        assert 26 == result

    def test_addWithNewLine(self):
        # Setup
        stringCalculatorClass = StringCalculatorClass()

        # Excercise
        result = stringCalculatorClass.add("1,2\n17")

        # Verify
        assert 20 == result


    def test_setNewDelimeter(self):
        # Setup
        stringCalculatorClass = StringCalculatorClass()

        # Excercise
        result = stringCalculatorClass.add("//;\n1;2;17\n5")

        # Verify
        assert 25 == result

    def test_setNewDelimeter(self):
        # Setup
        stringCalculatorClass = StringCalculatorClass()

        # Excercise
        result1 = stringCalculatorClass.newDelimiterSet("//;\n1;2;17\n5")
        result2 = stringCalculatorClass.newDelimiterSet("1;2;17\n5")

        # Verify
        assert True == result1
        assert False == result2

    def test_getNewDelimeter(self):
        # Setup
        stringCalculatorClass = StringCalculatorClass()

        # Excercise
        result = stringCalculatorClass.getNewDelimiter("//;\n1;2;17\n5")

        # Verify
        assert ';' == result

    def test_NegativeNumberRaisesException(self):
        # Setup
        stringCalculatorClass = StringCalculatorClass()
        exceptionRaised = False

        # Excercise
        try:
            result = stringCalculatorClass.add("-1")
        except Exception:
            exceptionRaised = True
        # Verify
        assert True == exceptionRaised


    def test_NegativeNumberRaisesExceptionWithMessage(self):
        # Setup
        stringCalculatorClass = StringCalculatorClass()
        exceptionRaised = False
        exceptionMessage = ""

        # Excercise
        try:
            result = stringCalculatorClass.add("-1")
        except Exception as err:
            exceptionMessage = err
            exceptionRaised = True
        # Verify
        assert True == exceptionRaised
        assert 'negatives not allowed' == exceptionMessage.args[0]

if __name__ == '__main__':
    unittest.main()
