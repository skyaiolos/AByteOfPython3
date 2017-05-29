#!/usr/bin/python
# Filename: using_dict.py

# 'ab' is short for 'a'ddress'b'ook

ab = {'Swaroop': 'swaroop@swaroopch.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }

for k, v in ab.items():
    print(f"{k}: {v}")
print()

print("Swaroop's address is", ab['Swaroop'])
# Deleting a key-value pair
del ab['Spammer']

print(f'After del "Spammer," ->There are {len(ab)} contacts in the address-book\n')

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

# OR ab.fromkeys('Guido')
if ab.fromkeys('Guido'):
    print("\nGuido's address is", ab['Guido'])
