from __future__ import nested_scopes


message = "hello world"
print(message)

message = "hello python crash course"
print(message)

name = "ada lovelace"
print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = f"{ first_name } { last_name }"
print(f"Hello { full_name.title() }!")

print("\tPython")

print("\nPython\nC#")

with_whitespace = "        python     "
print(with_whitespace)
print(with_whitespace.strip())

my_google = "www.google.com"
print(my_google.removeprefix("www.").removesuffix(".com"))

nest_aposttrophe_like_this = "Mike's python program"
print(nest_aposttrophe_like_this)

print(3 * .1)

# any float in an operation with integer always results in a float
print(5/2.5)

# Python doesn' have internal constants but you should write them as ALL_CAPS
MY_CONSTANT = 5000
