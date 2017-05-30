#!/usr/bin/python
# Filename: inherit.py
"""
12.7 继承
面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是
通过继承机制。继承完全可以理解成类之间的类型和子类型关系。
假设你想要写一个程序来记录学校之中的教师和学生情况。他们有一些共同属
性，比如姓名、年龄和地址。他们也有专有的属性，比如教师的薪水、课程和假期，
学生的成绩和学费。
你可以为教师和学生建立两个独立的类来处理它们，但是这样做的话，如果要增
加一个新的共有属性，就意味着要在这两个独立的类中都增加这个属性。这很快就会
显得不实用。
一个比较好的方法是创建一个共同的类称为 SchoolMember 然后让教师和学生的
类继承这个共同的类。即它们都是这个类型（类）的子类型，然后我们再为这些子类
型添加专有的属性。
使用这种方法有很多优点。如果我们增加/改变了 SchoolMember 中的任何功能，
它会自动地反映到子类型之中。例如，你要为教师和学生都增加一个新的身份证域，
那么你只需简单地把它加到 SchoolMember 类中。然而，在一个子类型之中做
的改动不会影响到别的子类型。另外一个优点是你可以把教师和学生对象都作为
SchoolMember 对象来使用，这在某些场合特别有用，比如统计学校成员的人数。一
个子类型在任何需要父类型的场合可以被替换成父类型，即对象可以被视作是父类的
实例，这种现象被称为 多态现象。
另外，我们会发现在重用父类的代码的时候，我们无需在不同的类中重复它。而
如果我们使用独立的类的话，我们就不得不这么做了。
在上述的场合中，SchoolMember 类被称为基本类或超类。而 Teacher 和 Student
类被称为导出类或子类。
现在，我们将学习一个例子程序。

"""


class SchoolMember:
    '''Represent any school member.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'(Initialize SchoolMember:{self.name})')

    def get_info(self):  # func named ,动词_名词
        '''Tell my details.'''
        print(f'Name:"{self.name}" Age:"{self.age}"')


class Teacher(SchoolMember):
    '''Repressent a teacher.'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f'(Initialized Teacher:{self.name})')

    def get_info(self):
        SchoolMember.get_info(self)
        print('Salary:"{0:d}"'.format(self.salary))


class Student(SchoolMember):
    '''Represents a student'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f'(Initialized Student:{self.name})')

    def get_info(self):
        SchoolMember.get_info(self)
        print('Marks:"{0:d}"'.format(self.marks))


def main():
    t = Teacher('Mrs.Shrividya', 30, 30000)
    s = Student('Swaroop', 25, 75)

    print()  # pirnts a blank line

    members = [t, s]
    for member in members:
        member.get_info()  # work for both Teacher and Students


if __name__ == '__main__':
    main()
else:
    print("inherit.py was imported!")
