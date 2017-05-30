#!/usr/bin/python
# Filename: objvar.py
"""
12.6 类和对象变量
我们已经讨论了类与对象的功能部分，现在我们来看一下它的数据部分。事实
上，它们只是与类和对象的名称空间绑定的普通变量，即这些名称只在这些类与对象的前提下有效。

有两种类型的域 —— 类的变量和对象的变量，它们根据是类还是对象拥有这个
变量而区分。
类的变量由一个类的所有对象（实例）共享使用。只有一个类变量的拷贝，所以
当某个对象对类的变量做了改动的时候，这个改动会反映到所有其他的实例上。
对象的变量由类的每个对象/实例拥有。因此每个对象有自己对这个域的一份拷
贝，即它们不是共享的，在同一个类的不同实例中，虽然对象的变量有相同的名称，
但是是互不相关的。通过一个例子会使这个易于理解。

"""


class Robot:
    '''Represents a robot, with a name.'''

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        '''Initializes the data.'''
        self.name = name
        print(f'(Initialize {self.name})')

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def __del__(self):
        '''I am del'''
        print(f'{self.name} is being destroyed!')

        Robot.population -= 1

        if Robot.population == 0:
            print(f'{self.name} was the last one.')
        else:
            print('There are still {0:d} robots working.'.format(Robot.population))

    def sayHi(self):
        '''Greeting by the robot.

        Yeah, they can do that.'''
        print(f'Greetings, my master call me {self.name}.')

    def howMany():
        '''Prints the current population.'''
        print('We have {0:d} robots.'.format(Robot.population))
        print()

    howMany = staticmethod(howMany)


def main():
    droid1 = Robot('R2-D2')
    droid1.sayHi()
    Robot.howMany()

    droid2 = Robot('C-3P0')
    droid2.sayHi()
    Robot.howMany()

    print("Robots can do some work here.\n")
    print("Robots have finished their work. So let's destroy them.")

    del droid1
    del droid2

    Robot.howMany()


if __name__ == '__main__':
    main()
else:
    print("objvar.py was imported!")
