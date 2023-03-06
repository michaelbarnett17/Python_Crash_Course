# the program will wait at input, then assign it to the left hand side
name = input("Please enter your name: ")
print(f"Hello { name }!")

# input is always a string, need to cast numbers
age = input("how old are you? ")

if int(age) >= 18:
    print("You are old enought to vote")
else:
    print("YOu are not old enough to vote")

current_number = 1

while current_number < 5:
    print(current_number)
    current_number += 1

# multiline prompt
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


# using a flag
prompt2 = "\nTell me something, and I will repeat it back to you:"
prompt2 += "\nEnter 'quit' or press Enter to end the program. "


active = True

while active:
    message = input(prompt2)
    if message == 'quit':
        active = False
    if message == "":
        active = False

# using continue

counter = 1

while counter < 100:
    if counter > 2 and counter < 99:
        counter += 1
        continue

    print(counter)
    counter += 1

# don't modify a list with iterating with a for loop
# use a while loop instead

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()
    print(f"Confirming user { user }")
    confirmed_users.append(user)

print(confirmed_users)

# remove all occurances of item in list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)