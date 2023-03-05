cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car)

# ignore case
print("AAA".lower() == "aaa")

## multiple conditions
age = 19

if age > 17 and age < 25:
    print("in college")
else:
    print("not in college")

# check if value is in list

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

print('mushrooms' in requested_toppings)

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"We have { requested_topping }.")
    else:
        print(f"Sorry we don't have any { requested_topping}.'")

# check if vale NOT in list

banned_users = ['andrew', 'carolina', 'david']
user = 'emily'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print(f"You are banned { user.title() }!")

# elif

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${ price }.")

# check for empty list

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding { requested_topping } to the pizza.")
    print("\nFinished making your pizza")
else:
    print("Are you sure you want a plain pizza?")
