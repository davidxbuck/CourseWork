#
class Employee:
    # method
    employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = "{}.{}@company.com".format(first, last).lower()

        Employee.employees += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    def __repr__(self):
        return "('{}', '{}', {})".format(self.first, self.last, self.salary)

    def __str__(self):
        return "{} {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.salary + other.salary # silly example, but it's about the principle

    def __len__(self):
        return len(self.fullname()) # another silly example

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split('-')
        return cls(first, last, salary)

    # logically grouped with the class but doesn't access class or instance data
    @staticmethod
    def is_workday(day):
        return False if day.weekday() == 5 or day.weekday() == 6 else True

class Developer(Employee):
    raise_amount = 1.2

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        # Employee.__init__(self, first, last, salary) can also be used in some circumstances
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees==None:
            self.employees=[]
        else:
            self.employees =employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)


    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('>', emp.fullname())

emp1 = Employee('David', 'Buck', 100000)
emp2 = Employee('Fred', 'Bloggs', 50000)
Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print()

emp1.raise_amount = 1.06

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print()

Employee.raise_amount = 1.08

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print()

emp_str_1 = "Bob-Jones-25000"
emp3 = Employee.from_string(emp_str_1)  # using a class method as an alternative constructor

print(emp3.fullname(), emp3.email)
print(Employee.employees)


import datetime

my_date = datetime.date(2019, 3, 29)

print(Employee.is_workday(my_date))

print(help(Developer))

dev1 = Developer('David', 'Buck', 100000, 'Python')
dev2 = Developer('Fred', 'Bloggs', 50000, "C++")

print(dev1.salary)
dev1.apply_raise() # Raise amount is now picked up from the Developer class, not inherited from the base class
print(dev1.salary)

print(dev1.email, dev1.prog_lang)

mgr1 = Manager('Fay', 'Brexit', 200000, [dev1])

print()
print(mgr1.email)
mgr1.print_emps()
print()

mgr1.add_emp(dev2)
mgr1.print_emps()
print()

mgr1.remove_emp(dev1)
mgr1.print_emps()

print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))

print(issubclass(Manager, Employee))
print()
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))
print(issubclass(Employee, Developer))

print(emp1)
print(repr(emp1))
print(len(emp1))
print(emp1 + emp2)