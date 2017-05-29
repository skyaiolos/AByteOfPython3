#!/usr/bin/python
# Filename: func_local.py
x = 50


def func(x):
    print('x is', x)
    x += 2
    print('After run x+=2, changed local x to', x)


print("Demo for the local parameter".center(50, '-'))
func(x)
print('x is still', x)
