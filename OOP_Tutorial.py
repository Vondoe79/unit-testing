# import sta

import datetime

class Employee:
    """Class variables are variables that as shared among all instances of a class.
        they should & must be the same for each instance of the class. (e.g. annual raise amount).
    """
    # example1 - class variable
    numb_of_empls = 0

    # example2 of a class variable
    raise_amt = 1.03

    def __init__(self, first, last, pay):
        """You may think of this as 'initialize' or 'constructor'.

            Methods within a class automatically receive the instance as the first argument.
                By conversion this is first argument is called 'self'.
                And then you can add any other arguments as deem fit.

        """
        # Now let's set the 'instance variables' which must be unique for each instance of a class; like
        # our names, pay, email address, etc. using a class method/function

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.numb_of_empls += 1

    # If we have to perform certain 'Actions' which must be repetitive,
    # then we should think of creating functions/methods to do that job
    def fullname(self):
        """function to return Employee class instance
        full name.
        """
        return f'{self.first}, {self.last}'

    def apply_raise(self):
        """An example of a class variable wrapped inside a regular method.
            1. we can either access the class variables via the class itself OR
            2. access them via an instance of the class(self).
                3. using point (2) instead of (1) allows to makes changes to class instances if need be.        """
        # self.pay =  self.pay * Employee.raise_amount # via the class itself
        self.pay = int(self.pay) * self.raise_amt  # via the class instance

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        """Using the @classmethod method as alternative constructors to create objects
        :arg - cls represents the class
            emp_str reprsents the string value that is passed to the method.
        """
        fname, lname, pay, = emp_str.split('-')  # the last comma after pay makes the assignment a list
        return cls(fname, lname, pay)

    @staticmethod
    def is_workday(day):
        """These methods are neither regular nor class methods. They may not depend on any instance or class variables.
            They, but only have some logical connection with the class. They also do not take the instance(self) nor
            class(cls) arguments. Instead, just pass in the arguments that you want to work with.

        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Inheritance & Sub-classes in Python
class Developer(Employee):
    """This child class inherited from the parent class, Employee.
        we can customize certain things in this class like a different
        raise amount for our developers from 4% to 10%.
    """
    raise_amt = 1.10

    # if we want to give/initiate our Developer sub-class/child class with more information
    # than their parent class can handle, we may need to give our sub-class its own "__init__" method.

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # 1-way to call the parent class' "__init__" method
        # Employee.__init__(self, first, last, pay) # a 2nd way to call the parent class' "__init__" method
        self.prog_lang = prog_lang


# Let's class another sub-class that will inherit from the Employee class
class Manaager(Employee):
    """this class will also have it's own __init__ method"""

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        """This method adds new employee to the manager class
        Args: emp - the newly added employee"""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        """This method removes an employee from the manager class."""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            return emp.fullname()


# create Employee
emp_1 = Employee('Von', 'Doe', 50000)
emp_2 = Employee('Test', 'User', 60000)

# create Developer instance variable
dev_1 = Developer('Emmanuel', 'Adjavor', 50000, 'Python')
dev_2 = Developer('Paul', 'Adjavor', 60000, 'Julia')

# create Manager instance variab
mgr_1 = Manaager('Clifford', 'Adjavor', 90000, [dev_1])

# print the Employee instance class
# print(emp_1)
# print(emp_2)

# An example of manual assignation of "instance variables/data/info/" -
# Instance variables contain DATA that is unique to each instance
# emp_1.first = 'hayford'
# emp_1.last = 'adjavor'
# emp_1.email = 'hayford.adjavor@gmail.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@gmail.com'
# emp_2.pay = 60000

# How to create a new employee object/instance when you get the information in the form of a string value
# using our Employee class: Example below:-
emp_str_1 = 'kofi-doe-70000'
emp_str_2 = 'samar-alhihi-80000'
emp_str_3 = 'alex-adjavor-25000'

# first we split on the hyphen (-)
# fname, lname, pay, = emp_str_1.split('-')

# Then, we create the instance of the new employee using the class, 'Employee'
new_emp_1 = Employee.from_string(emp_str_1)

breakingpoint_ = 0

# print to inspect object
print(new_emp_1.email)
print(new_emp_1.pay)

breakingpt_ = 1

print(new_emp_1.apply_raise())

# Printing Function  calls or instance and/or instance Variable calls
# print an attribute variable (email) of the Employee instance class
print(emp_1.email)
print(emp_2.email)

# doing a certain actions manually, but
# this could be done using a class method/function as in above.
# print(f'{emp_1.first}, {emp_1.last}')

# print the sane action using the class method creative above
print(emp_1.fullname())
print(emp_2.fullname())

# we can also run the above as follows
print(emp_1.fullname())  # we can run a method on a class instance OR
print(Employee.fullname(emp_1))  # run method on the Employee class and pass the respective instance of the class to it.

# accessing the name space of a class instance
print(emp_1.__dict__)

# check out the class variable function before and after the raise
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# let's call the class method to change the "raise_amt" cls variable
# to a new global value
Employee.set_raise_amount(1.08)

# access the class variable(s) via the class or class instance
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(Employee.numb_of_empls)

# access the @staticmethod function
my_date = datetime.date(2021, 10, 31)
print(Employee.is_workday(my_date))

breakingpt_ = 2

# print to inspect the developer class
# print the Developer instance class: "Method Resolution Order"
print(dev_1.email)
print(dev_1.prog_lang)
print(dev_1.pay)

# check out Python's "Method Resolution Order"
# print(help(Developer))
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

breakingpt_ = 3

print(f'attributes of mgr_1 is:++++++++> {mgr_1}')
print(f'attributes of mgr_1 is:++++++++> {mgr_1.email}')
mgr_1.add_emp(dev_2)
print(mgr_1.print_emps())

breakingpt_ = 4
