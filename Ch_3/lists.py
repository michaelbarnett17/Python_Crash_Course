teams = ["bucks", "bulls", "pistons", "heat", "celtics"]

print(teams)

print(type(teams))

print(teams[0])

# last item
print(teams[-1])

teams[1] = "lakers"
print(teams)

teams.append("hornets")
print(teams)

teams.insert(2, "spurs")
print(teams)

# remove by value
teams.remove("lakers")
print(teams)

# remove by index
del teams[0]
print(teams)

# remove last item and return
popped_team = teams.pop()
print(popped_team)

# pop from anywhere index
popped_from_index = teams.pop(1)
print(popped_from_index)

# WRONG WAY TO SORT - THE .sort() doesn't return anything
wrong = [1, 33, 22, 12, 9]
wrong = wrong.sort()
print(wrong)

# CORRCT WAY TO SORT
right = [1, 33, 22, 12, 9]
right.sort()
print(right)

# ANOTHER CORRECT WAY
original = [1, 33, 22, 12, 9]
now_sorted = sorted(original)
print(original)
print(now_sorted)

# SAME FOR REVERSE
myNumbers = [1, 33, 22, 12, 9]
myNumbers.reverse()
print(myNumbers)

# LENGTH
print(f"the length of myNumbers is { len(myNumbers) }")