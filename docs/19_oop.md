```python
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
```
Output:
```
23
2 employees:
Abolfazl born on 1996, salary=12345
Sarah born on 1997, salary=54321
```

**Built-in** class functions:
```python
# return 'True' if emp1 has 'age' attribute otherwise 'False'
hasattr(emp1, 'age')
# return 'age' attribute value
getattr(emp1, 'age')
# set 'age' attribute value to 24
setattr(emp1, 'age', 24)
# delete 'age' attribute from emp1 object
delattr(emp1, 'age')
```
**method/attribute** started with **double-underscore** (`__`) is **private**
to the class and will not be inherited from subclass and is
accessible with `_class__attribute` inside subclass.

**method/attribute** started with **underscore** (`_`) is **protected**, but is
accessible from subclass and directly.

Inheritance:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_details(self):
        return "name={} age={}".format(self.name, self.__age)


class Student(Person):
    def __init__(self, name, age, branch, year):
        self.branch = branch
        self.year = year
        # also 'Person.__inti__(name, age)' can be used
        super().__init__(name, age)

    def get_details(self):
        return "name={} age={} branch={} year={}".format(
            self.name, self._Person__age, self.branch, self.year)


person = Person('Sarah', 23)
student = Student('Abolfazl', 24, 'CSE', 2014)
print(person.get_details())
print(student.get_details())
```
Output:
```
name=Sarah age=23
name=Abolfazl age=24 branch=CSE year=2014
```
