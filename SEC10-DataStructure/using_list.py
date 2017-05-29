#!/usr/bin/python
# Filename: using_list.py

# This is my shopping list
shop_list = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shop_list), 'items to purchase.')

print('These items are: ', end=' ')

for item in shop_list:
    print(item, end=', ')

print('\n\nI also have to buy rice.')
shop_list.append('rice')
print('My shopping list is now', shop_list)

print('\nI will sort my list now')
shop_list.sort()
print('Sorted shopping list is: ', shop_list)

print('\nThe first item I will buy is: ', shop_list[0])
del_item = shop_list[0]
del shop_list[0]
print('No need to bug the', del_item)
print('My shopping list is now:', shop_list)
