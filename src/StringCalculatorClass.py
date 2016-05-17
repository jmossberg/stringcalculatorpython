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

        if self.newDelimiterSet(newString):
            self.delimiter = self.getNewDelimiter(newString)
            return newString[self.DELIMITER_POSITION+1:]

        return newString

    def newDelimiterSet(self, newString):
        return (newString[0:self.DELIMITER_POSITION] == "//") and (newString[self.DELIMITER_POSITION+1] == '\n')

    def getNewDelimiter(self, newString):
        return newString[self.DELIMITER_POSITION]

    def add(self, newString):

        returnvalue = 0
        self.negative_numbers = []

        if(len(newString) > 0):
            stringWithoutDelimiter = self.setDelimiter(newString)
            returnvalue = self.splitLines(stringWithoutDelimiter)
            if len(self.negative_numbers) > 0:
                strNumbers = ""
                for number in self.negative_numbers:
                    strNumbers += str(number) + ", "
                strNumbers = strNumbers[0:len(strNumbers)-2]
                raise Exception('negatives not allowed: ' + strNumbers)


        return returnvalue
