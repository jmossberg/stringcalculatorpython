class StringCalculator:

    NEW_DELIMITER_POSITION = 2
    DEFAULT_DELIMITER = ","
    _delimiter = DEFAULT_DELIMITER
    _negative_numbers = []

    def _text_to_integer(cls, number):

        numberAsInteger = int(number)

        if numberAsInteger < 0:
            cls._negative_numbers.append(numberAsInteger)
            numberAsInteger = 0

        return numberAsInteger

    def _sum_of_numbers_in_line(cls, newString):

        newstringsum = 0

        numbers = newString.split(cls._delimiter)

        for number in numbers:
            newstringsum += cls._text_to_integer(number)

        return newstringsum

    def _split_lines(cls, newString):

        sum = 0
        lines = newString.splitlines()

        for line in lines:
            sum += cls._sum_of_numbers_in_line(line)

        return sum

    def _set_new_delimiter(cls, newString):

        if cls._is_new_delimiter_set(newString):
            cls._delimiter = cls._get_new_delimiter(newString)

    def _get_string_without_delimiter(cls, newString):
        if cls._is_new_delimiter_set(newString):
            return newString[cls.NEW_DELIMITER_POSITION + 2:]
        return newString

    def _is_new_delimiter_set(cls, newString):
        return (newString[0:cls.NEW_DELIMITER_POSITION] == "//") and (newString[cls.NEW_DELIMITER_POSITION + 1] == '\n')

    def _get_new_delimiter(cls, newString):
        return newString[cls.NEW_DELIMITER_POSITION]

    def _create_error_message(cls, negative_numbers):

        error_message = 'negatives not allowed: '

        for number in negative_numbers:
            error_message += str(number) + ", "

        # Remove comma and space after the last negative number
        error_message = error_message[0:len(error_message) - 2]

        return error_message

    def add(cls, numbers_as_string):

        sum_of_numbers = 0
        cls._negative_numbers = []
        _delimiter = cls.DEFAULT_DELIMITER

        if len(numbers_as_string) == 0:
            return sum_of_numbers

        if cls._is_new_delimiter_set(numbers_as_string):
            cls._set_new_delimiter(numbers_as_string)
            string_without_delimiter = cls._get_string_without_delimiter(numbers_as_string)
        else:
            string_without_delimiter = numbers_as_string

        sum_of_numbers = cls._split_lines(string_without_delimiter)

        if len(cls._negative_numbers) > 0:
            error_string = cls._create_error_message(cls._negative_numbers)
            raise Exception(error_string)

        return sum_of_numbers
