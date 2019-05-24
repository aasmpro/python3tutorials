class Employee:
    """common base class for all employees"""
    # class variables
    __count, __all = 0, []

    # class constructor
    def __init__(self, name, born_year, salary):
        self.__name = name
        self.__born_year = born_year
        self.__salary = salary
        Employee.__all.append(self)
        Employee.__count += 1

    def age(self, current_year):
        return current_year - self.__born_year

    @classmethod
    def all_str(cls):
        result = "{} {}:".format(
            cls.__count, 'employees' if cls.__count > 1 else 'employee')
        for employee in cls.__all:
            result += '\n' + str(employee)
        return result

    def __str__(self):
        return "{} born on {}, salary={}".format(
            self.__name, self.__born_year, self.__salary)


emp1 = Employee("Abolfazl", 1996, 12345)
emp2 = Employee("Sarah", 1997, 54321)
print(emp1.age(2019))
print(Employee.all_str())
