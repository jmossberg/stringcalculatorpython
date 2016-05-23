import unittest

from src.StringCalculator import StringCalculator


class TestStringCalculatorClass(unittest.TestCase):
    def test_add_empty_string(self):
        # Setup
        string_calculator = StringCalculator()

        # Exercise
        result = string_calculator.add("")

        # Verify
        assert 0 == result

    def test_add_one(self):
        # Setup
        string_calculator = StringCalculator()

        # Exercise
        result = string_calculator.add("1")

        # Verify
        assert 1 == result


    def test_add_two(self):
        # Setup
        string_calculator = StringCalculator()

        # Exercise
        result = string_calculator.add("2")

        # Verify
        assert 2 == result


    def test_add_one_and_two(self):
        # Setup
        string_calculator = StringCalculator()

        # Exercise
        result = string_calculator.add("1,2")

        # Verify
        assert 3 == result


    def test_add_five_numbers(self):
        # Setup
        string_calculator = StringCalculator()

        # Exercise
        result = string_calculator.add("1,2,17,4,1,1")

        # Verify
        assert 26 == result

    def test_add_with_new_line(self):
        # Setup
        string_calculator = StringCalculator()

        # Exercise
        result = string_calculator.add("1,2\n17")

        # Verify
        assert 20 == result

    def test_is_new_delimiter_set(self):
        # Setup
        string_calculator = StringCalculator()

        # Exercise
        result1 = string_calculator._is_new_delimiter_set("//;\n1;2;17\n5")
        result2 = string_calculator._is_new_delimiter_set("1;2;17\n5")

        # Verify
        assert True == result1
        assert False == result2

    def test_get_new_delimiter(self):
        # Setup
        string_calculator = StringCalculator()

        # Exercise
        result = string_calculator._get_new_delimiter("//;\n1;2;17\n5")

        # Verify
        assert ';' == result

    def test_get_string_without_delimiter(self):
        # Setup
        string_calculator = StringCalculator()

        # Exercise
        result = string_calculator._get_string_without_delimiter("//;\n1,2")

        # Verify
        assert "1,2" == result

    def test_call_add_with_new_delimiter(self):
        # Setup
        string_calculator = StringCalculator()

        # Exercise
        result = string_calculator.add("//;\n1;2;17\n5")

        # Verify
        assert 25 == result

    def test_create_error_message_for_negative_numbers(self):
        # Setup
        string_calculator = StringCalculator()
        negative_numbers = [-1, -2, -3]

        # Exercise
        result = string_calculator._create_error_message(negative_numbers)

        # Verify
        assert 'negatives not allowed: -1, -2, -3' == result

    def test_negative_numbers_raises_exception(self):
        # Setup
        string_calculator = StringCalculator()
        exception_raised = False

        # Exercise
        try:
            result = string_calculator.add("-1")
        except Exception:
            exception_raised = True

        # Verify
        assert True == exception_raised


    def test_negative_number_raises_exception_with_message(self):
        # Setup
        string_calculator = StringCalculator()
        exception_raised = False
        exception_message = ""

        # Exercise
        try:
            result = string_calculator.add("-1")
        except Exception as err:
            exception_message = err
            exception_raised = True

        # Verify
        assert True == exception_raised
        assert 'negatives not allowed: -1' == exception_message.args[0]

    def test_multiple_negative_numbers(self):
        # Setup
        string_calculator = StringCalculator()
        exception_raised = False
        exception_message = ""

        # Exercise
        try:
            result = string_calculator.add("2,-1,4,-2")
        except Exception as err:
            exception_message = err
            exception_raised = True

        # Verify
        assert True == exception_raised
        assert 'negatives not allowed: -1, -2' == exception_message.args[0]


if __name__ == '__main__':
    unittest.main()
