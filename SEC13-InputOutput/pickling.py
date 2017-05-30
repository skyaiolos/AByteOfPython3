#!/usr/bin/python
# Filename: pickling.py

import pickle

# the name of the file where we will store the object
shop_list_file = 'shoplist.data'
# the list of things to buy
shop_list = ['apple', 'mango', 'carrot']
shop_list1 = ['name', 'age', 'sex']

# Write to the file
f = open(shop_list_file, 'wb')
pickle.dump(shop_list, f)  # dump the object to a file
pickle.dump(shop_list1, f)
f.close()

del shop_list  # detroy the shoplist variable
del shop_list1

# Read back from the storage
with open(shop_list_file, 'rb') as f:
    while True:
        try:
            stored_list = pickle.load(f)  # load the object from the file
        except EOFError:
            break
        print(stored_list)
