magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)


for magician in magicians:
    print(f'{ magician.title() }, that was a great trick')
    print(f'I can\'t wait to see your next trick, { magician.title() }!\n')

print('That was a great magic show\n')

for value in range(1,5):
    print(value)

# index in loop with external variable
count = 0;

for magician in magicians:
    print(count, magician)
    count += 1
    
# index for loop (pythonic way)
for i, magician in enumerate(magicians):
    print(i, magician)

# range to make a list
myNumbers = list(range(1,6));

print(myNumbers)

# range with step size
evenNumbers = list(range(0, 50, 2));

print(evenNumbers)

squares = []

for value in range(1, 11):
    squares.append(value**2)

print(type(squares))
print(squares)

# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# prints first 3 players (stops before index 3)
print(players[:3])

# print from index 1 to end
print(players[1:])

# print index 1 though 3 (stops before index 3)
print(players[1:3])

# print last 3 players
print(players[-3:])

print()

# copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')

print(my_foods)
print(friend_foods)

print()

# tuple is immutable list that care store various data types
myItems = ('pizza', 10, 5.55)

for item in myItems:
    print(item)

# tuples are immutable!
# myTuple[1] = 11;

# but you can overwrite a tuple (reassign variable)
myItems = (1, 2, 3, 4, 5)

for item in myItems:
    print(item)