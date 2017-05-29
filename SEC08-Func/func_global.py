#!/usr/bin/python
# Filename: func_global.py

x = 50


def func():
    global x
    x = 2
    print('Changed global x to', x)


print(f'--Before global x is {x}')

func()
print('Value of x is', x)
print(f'--After global x is {x}')
