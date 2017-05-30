"""
#  Script Description:
    Training for the inherit

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/5/30
# File name ->

class SchoolMember:
    def __init__(self, name='', age=0, gender='male'):
        self.name = name
        self.age = age
        self.gender = gender
        # print(f"(initialization the SchoolMember: {self.name})")
        print(f"(initialization the {__class__.__name__}: {self.name})")

    def __str__(self):
        return f"(initialization the {self.__class__.__name__}:{self.name})"

    def get_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


class Teacher(SchoolMember):
    def __init__(self, name='', age=30, gender='', salary=10000):
        SchoolMember.__init__(self, name, age, gender)
        self.salary = salary

    def get_info(self):
        SchoolMember.get_info(self)
        print('Salary: {0:d}'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name='', age=0, gender='', marks=0):
        SchoolMember.__init__(self, name, age, gender)
        self.marks = marks

    def get_info(self):
        SchoolMember.get_info(self)
        print('Mars: {0:d}'.format(self.marks))


def main():
    t = Teacher("Mark", 30, 'Male', 20000)
    print(t)
    s = Student("Xixi", 4, 'Female', 98)
    print(s)

    print()
    members = [t, s]

    for member in members:
        member.get_info()


if __name__ == '__main__':
    main()
