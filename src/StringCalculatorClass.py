class StringCalculatorClass:

    DELIMITER_POSITION = 2
    DEFAULT_DELIMITER = ","
    delimiter = DEFAULT_DELIMITER
    negative_numbers = []

    def textToInteger(self, number):

        numberAsInteger = int(number)

        if numberAsInteger < 0:
            self.negative_numbers.append(numberAsInteger)
            numberAsInteger = 0

        return numberAsInteger

    def addNonEmptyString(self, newString):

        newstringsum = 0

        numbers = newString.split(self.delimiter)

        for number in numbers:
            newstringsum += self.textToInteger(number)

        return newstringsum

    def splitLines(self, newString):

        sum = 0
        lines = newString.splitlines()

        for line in lines:
            sum += self.addNonEmptyString(line)

        return sum

    def setDelimiter(self, newString):

        if self.isNewDelimiterSet(newString):
            self.delimiter = self.getNewDelimiter(newString)

    def getStringWithoutDelimiter(self, newString):
        if self.isNewDelimiterSet(newString):
            return newString[self.DELIMITER_POSITION + 2:]
        return newString

    def isNewDelimiterSet(self, newString):
        return (newString[0:self.DELIMITER_POSITION] == "//") and (newString[self.DELIMITER_POSITION+1] == '\n')

    def getNewDelimiter(self, newString):
        return newString[self.DELIMITER_POSITION]

    def createErrorString(self, negative_numbers):

        if len(negative_numbers) > 0:
            strNumbers = ""
            for number in negative_numbers:
                strNumbers += str(number) + ", "
            strNumbers = strNumbers[0:len(strNumbers) - 2]
            return 'negatives not allowed: ' + strNumbers

        return ""

    def add(self, newString):

        returnvalue = 0
        self.negative_numbers = []

        if(len(newString) == 0):
            return returnvalue

        if(self.isNewDelimiterSet(newString)):
            self.setDelimiter(newString)
            stringWithoutDelimiter = self.getStringWithoutDelimiter(newString)

        else:
            stringWithoutDelimiter = newString

        returnvalue = self.splitLines(stringWithoutDelimiter)

        error_string = self.createErrorString(self.negative_numbers)

        if len(error_string) > 0:
            raise Exception(error_string)

        return returnvalue
