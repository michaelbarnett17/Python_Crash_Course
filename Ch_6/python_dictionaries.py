# dictionary
my_alien = { 
    'color': 'green',
    'points': 5
}

# use keys to get values
print(my_alien['color'])
print(my_alien['points'])

# add key/value pair to dictonary
my_alien['x_position'] = 0 

# modify values
my_alien['points'] = 10

print(my_alien)

# remove key/value pairs
del my_alien['points']

print(my_alien)


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

print(f"Sarah's favorite language is { favorite_languages['sarah'] }")

# use get for default if no key is found

points_value = favorite_languages.get('johnny', 'no favorite language is assigned')
print(points_value)


# loop though keys in a dictonary

for k in favorite_languages.keys():
    print(f"{ k }")

# loop though values in a dictonary
for v in favorite_languages.values():
    print(f"{ v }")

# loop though keys and values in a dictionary

for k, v in favorite_languages.items():
    print(f"{ k }'s favorite language is { v }")

if 'erin' not in favorite_languages.keys():
    print("Erin doesn't know how to program.")

# keys usually looped in order they were inserted, but you can sort then loop
for k in sorted(favorite_languages.keys()):
    print(f"{ k }")

# use set() to remove duplicates
[1, 2, 3, 4, 4, 3, 2, 1, 6, 100]
print(set([1, 2, 3, 4, 4, 3, 2, 1, 6, 100]))

# dictionaries inside a list
alien0 = { 
    'color': 'green',
    'points': 5
}

alien1 = { 
    'color': 'yellow',
    'points': 10
}

alien2 = { 
    'color': 'green',
    'points': 20
}

aliens = []

aliens.append(alien0)
aliens.append(alien1)
aliens.append(alien2)

print(aliens)

# use range to create many alien dictonaries in a list

aliens = []

for count in range(30):

    alien = { 
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }

    aliens.append(alien)

print(len(aliens))

# list in a dictonary

pizza = {
    'crust': 'thick',
    'toppings': ['green peppers', 'pepproni', 'sausage', 'mushrooms']
}

for k, v in pizza.items():
    print(f"{ k } : { v }")


# lists in dictonary, all values are lists

favorite_languages = {
      'jen': ['python', 'rust'],
      'sarah': ['c'],
      'edward': ['rust', 'go'],
      'phil': ['python', 'haskell'],
      }

for name, languages in favorite_languages.items():
    print(f"{ name }:", end=" ") #use end as 2nd print parmater to print on same line
    for item in languages:
        print(f" { item }", end=" ")
    print()

# dictonary inside a dictonary
# note items in dictonary have same structure, code would be harder if different
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }

for user_name, user_info in users.items():
    print(user_name)
    for info_type, info_value in user_info.items():
        print(f"\t{ info_type }: { info_value }")
