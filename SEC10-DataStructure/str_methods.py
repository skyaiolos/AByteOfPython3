#!/usr/bin/python
# Filename: str_methods.py

name = 'Swaroop'  # This is a string object

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
my_list = ['Brazil', 'Russia', 'India', 'China']

try:
    print(my_list.join(delimiter))

except AttributeError as e:
    print("AttributeError : ", e)

# try:
#     print(my_list.join(delimiter))
#
# except AttributeError as e:
#     raise e

# AttributeError: 'list' object has no attribute 'join'
