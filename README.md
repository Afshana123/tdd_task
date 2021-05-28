# TDD Task 

---

The exercise is as follows:

- [x] Create a new git hub repo and project in Pycharm.
- [x] Create tests for functions cm to inches, modular, triangle calculation and calculate %.
- [x] Write the code to pass all the tests.
- [X] create 2 files 1 for tests and 1 for functional code.
- [x] Apply OOP to achieve the desired results.

## My Solution

Installed pytest with the command `pip install pytest`. 

A new python test file was created, and a code was written as shown below in order to check and pass all the tests.

```python
import pytest
import unittest

from CalcTask import CalcTask

class Calctest_task(unittest.TestCase):

    calc = CalcTask()
# this will run first (should pass)
    def test_percentage(self): # naming convention is essential as 'test' is the word we need to use naming tests
        self.assertEqual(self.calc.percentage(25, 100), 25) # it will add them and check if it is 6

    def test_is_number_divisible(self):
        self.assertEqual(self.calc.is_number_divisible(11, 5), False)

    def test_cm_to_inches(self):
        self.assertEqual(self.calc.cm_to_inches(1), 0.39370079)

    def test_area_of_triangle(self):
        self.assertEqual(self.calc.area_of_triangle(10, 2), 10)
```
The command `python -m unittest` was run to run the test.

Another file was created with a class, and the functional code was written as according to the requirements of the task.

````python
class CalcTask:

    # Create a function that calculates the percentage
    def percentage(self, value1, value2):
        return (value1 / value2) * 100

    def is_number_divisible(self, value1, value2):
        if value1 % value2 == 0:
            return True
        else:
            return False

    def cm_to_inches(self, value1):
        return value1 * 0.39370079

    def area_of_triangle(self, height, base):
        return 1 / 2 * height * base

````
The command `python -m unittest` was run again to ensure all 4 tests pass.

- [x] All tests passed.




