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

# pass list to function
    
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_item = unprinted_designs.pop(0)
        print(f"Printing { current_item }")
        completed_models.append(current_item)

def show_completed_models(completed_models):
    print(f"The completed models are: { completed_models }. ")


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# pass a copy of a list so original list doesn't get modified

game_consoles = ["nintendo", "xbox", "playstation"]

def do_something(game_consoles):
    game_consoles = ["pc"]
    return game_consoles

print(do_something(game_consoles[:])) # use a slice to pass copy
print(game_consoles)

# pass arbitrary number of arguments (the asterisk makes a tuple containg all the values it recieveds)

def make_pizza(*toppings):
    print(toppings)

make_pizza("pepperoni")
make_pizza("pepperoni", "green olives")