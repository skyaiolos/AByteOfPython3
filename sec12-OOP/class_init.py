#!/usr/bin/python
# Filename: class_init.py
"""
    12.5 __init__ 方法
在 Python 的类中有很多方法的名字有特殊的重要意义。现在我们将学习 __init__
方法的意义。
__init__ 方法在类的一个对象被建立时，马上运行。这个方法可以用来对你的对
象做一些你希望的初始化。注意，这个名称的开始和结尾都是双下划线。
    这里，我们把 __init__ 方法定义为取一个参数 name（以及普通的参数 self）。在
这个 __init__ 里，我们只是创建一个新的域，也称为 name。注意它们是两个不同的
变量，尽管它们有相同的名字。点号使我们能够区分它们。
最重要的是，我们没有专门调用 __init__ 方法，只是在创建一个类的新实例的时
候，把参数包括在圆括号内跟在类名后面，从而传递给 __init__ 方法。这是这种方法
的重要之处。
现在，我们能够在我们的方法中使用 self.name 域。这在 sayHi 方法中得到了验
证。（译者注：__init__ 方法相当于 C++，Java，C# 中的构造函数）。

"""


class Person:
    def __init__(self, name=''):
        self.name = name
        print(f'inint {self.__class__.__name__}')

    def sayHi(self):
        print('Hello, my name is: ', self.name)


# This short example can also be written as Person('Swaroop').sayHi()
p = Person('Swarppp')
p.sayHi()
# Hello, my name is Swaroop
