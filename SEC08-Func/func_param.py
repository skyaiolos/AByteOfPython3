def printMax(a, b):
    if a > b:
        print(f'{a} > {b}, {a} is the maximum')
    elif a == b:
        print(f'{a} = {b} , {a} is equal to {b}')
    else:
        print(f'{a} < {b} , {b} is the maximum')


printMax(3, 4)  # directly give literal valuse

x = 5
y = 7

printMax(x, y)  # give variables as arguments
