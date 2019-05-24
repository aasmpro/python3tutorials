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
