# import only specific functions from pizza module

from pizza import make_pizza
from pizza import cook_pizza as cp

# use this to import all without using prefixes
#from pizza import *

make_pizza(12, "cheese", "pepperoni", "green peppers")

cp()