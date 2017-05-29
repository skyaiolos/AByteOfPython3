#!/usr/bin/python
# Filename: func_nonlocal.py

def func_outer():
    x = 2
    print('Before nonlocal, the x is', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('After nonlocal, changed local x to', x)


func_outer()
