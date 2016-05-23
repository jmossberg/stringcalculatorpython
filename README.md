This git repository contains one possible solution in Python 3 to the StringCalculator Kata

To import the project into PyCharm Community Edition 2016.1.2 in the "CodingDojoMossberg_160519" Virtual Machine:

```python
s = "Python syntax highlighting"
print s
```

1. Goto Start menu - System Tools - LXTerminal
1. Install git: `sudo apt-get install git`
   ```
   sudo apt-get install git
   ```
1. Enter password:
     {{{ codingdojo }}}
1. Goto Start menu - Programming - PyCharm
1. Select menu VCS - Checkout from Version Control - Git
1. Enter Git Repository URL:
     {{{ https://github.com/jmossberg/stringcalculatorpython.git }}}
1. Click on Clone
1. Answer Yes when asked "Would you like to open the directory /home/codingdojo/PycharmProjects/stringcalculatorpython?"
1. Select "Open in new window"
1. Open test_stringCalculatorClass.py in stringcalculatorpython -> test
1. Select menu Run - Edit configurations...
1. Click on + in the top left corner and select Python tests - Unittests
1. Click inside the Script: box and click on the ... button
1. Select test_stringCalculatorClass.py in the test folder
1. Click OK
1. Click on the green arrow in the top right corner to run the tests
