import unittest
from unittest.mock import patch
from employee_salary import Employee

class TesEmployeeSalary(unittest.TestCase):
    """针对Employee类的测试"""


    #传入的参数是说要覆盖的旧对象是内置的input函数
    @patch("builtins.input")
    def test_give_defalut_raise(self,mock_input):
        self.employee = Employee("chirs damned","$1000000")
        mock_input.return_value = 'q'
        self.employee.give_raise()
        self.assertEqual(self.employee._raise, 5000)

    #传入的参数是说要覆盖的旧对象是内置的input函数
    @patch("builtins.input")
    def test_give_custom_raise(self,mock_input):
        self.employee = Employee("chirs damned","$1000000")
        mock_input.return_value = '20000'
        self.employee.give_raise()
        self.assertEqual(self.employee._raise, 20000)

unittest.main()
