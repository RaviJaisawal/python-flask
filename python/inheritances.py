class Student:

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def getName(self):
        return "your name is {}".format(self.name)

    def getAge(self):
        return "your age is {}".format(self.age)

    @classmethod
    def imclass(cls,classname):
        return  "Hi I classmethod {} {}".format(cls , classname.age)

    @staticmethod
    def imstactic():
        return "I m static method"


class Employee(Student):

    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id = id


    def getId(self):
        return "your id is {}".format(self.id)



emp = Employee("spit",15,1)
print(emp.getId())
print(emp.imclass(emp))
print(emp.imstactic())
# print(Student.imstactic())
# print(Student.imclass())


