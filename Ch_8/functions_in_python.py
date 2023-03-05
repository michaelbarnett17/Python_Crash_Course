from distutils.command.build import build


def greet_user():
    print("Hello")

greet_user()

def greet_user(username):
    print(f"Hello { username }!")

greet_user("Michael")

# positional arguments
def describe_pet(animal_type, name, age):
    print(f"I have a { animal_type }, her name is { name } and she is { age } years old!")

describe_pet('dog', 'amy', 5)
describe_pet('dog', 'lucy', 5)

# keyword arguments

# keyword arguments (position doesn't matter)
def describe_pet(animal_type, name, age):
    print(f"I have a { animal_type }, her name is { name } and she is { age } years old!")
     
describe_pet(animal_type = 'dog', name = 'amy', age = 5)

describe_pet(name = 'amy', age = 5, animal_type = 'dog')

# default parmaters (need to be the last parmaters)
def describe_pet(name, age, animal_type = 'dog'):
    print(f"I have a { animal_type }, her name is { name } and she is { age } years old!")

describe_pet('kelly', 15)

# return value
def get_formatted_name(first_name, last_name):
    return f"{ first_name} { last_name }".title()

print(get_formatted_name('john', 'doe'))

# return a dictonary, optional paramater

def build_person(first_name, last_name, age=""):

    if age:
        person = {

            'first_name': first_name,
            'last_name': last_name,
            'age': age
        }
    else:
        person = {

        'first_name': first_name,
        'last_name': last_name,

        }

    return person

print(build_person('jimi', 'hendrix', 27))
print(build_person('jimi', 'hendrix'))

# calling a function in a while loop
while True:
    print("\nWhat is your name?")
    print("\nEnter q at any time to quit?")
    f_name = input("First Name: ")

    if f_name == 'q':
        break

    l_name = input("Last Name: ")

    if l_name == 'q':
        break

    print(get_formatted_name(f_name, l_name))