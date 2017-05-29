#!/usr/bin/python
# Filename: class_init.py
"""
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
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print('Hello, my name is', self.name)


# This short example can also be written as Person('Swaroop').sayHi()
p = Person('Swaroop')
p.sayHi()
# Hello, my name is Swaroop
