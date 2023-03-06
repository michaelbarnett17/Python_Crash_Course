def make_pizza(size, *toppings):
    print(f"Making a { size } inch pizza with the following toppings: ", end="")
    for topping in toppings:
        print(topping, end=", ")


def cook_pizza():
    print(f"\nCooking your pizza now")