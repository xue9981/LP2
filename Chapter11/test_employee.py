from employee import Employee
import unittest

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.my_employee_1 = Employee('xue', 'junfeng', 100000)
        self.my_employee_2 = Employee('ma', 'yun', 0)

    def test_give_default_raise(self):
        self.my_employee_1.give_raise()

    def test_give_costom_raise(self):
        self.my_employee_2.give_raise(1)

unittest.main()
