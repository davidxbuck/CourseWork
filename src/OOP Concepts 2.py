class Employee:
    # method
    employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

        Employee.employees += 1

    @property  # acts as a getter
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last).lower()

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None


emp1 = Employee('David', 'Buck', 100000)
emp2 = Employee('Fred', 'Bloggs', 50000)


emp1.first = 'Jim' # Doesn't update the email if you just change the first name
emp1.fullname = "John Smith" # will fail without the setter

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname