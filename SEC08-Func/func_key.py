#!/usr/bin/python
# Filename: func_key.py

def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


print("Demo for def func(a, b=5, c=10)".center(40, '~'))
print('func(3, 7)'.center(20, '-'))
func(3, 7)
print()

print('func(25, c=24)'.center(20, '-'))
func(25, c=24)
print()

print('func(c=50, a=100)'.center(20, '-'))
func(c=50, a=100)
