#11-3
class Employee():
    """docstring for Employee"""

    def __init__(self, name,salary):
        """initialize the name and salary"""
        self.name = name.title()
        self.salary = salary


    def give_raise(self):
        #self._raise = 5000
        print("\nDefault raise or custom raise?")
        self._raise = input("If you want a custom raise? Please enter the raise\
number. If not,please enter 'q'. ")
        if self._raise =='q':
            self._raise = 5000
        else:
            self._raise = int(self._raise)
        #print(self._raise)

#employee = Employee("chirs damned","$1000000")
#employee.give_raise()
