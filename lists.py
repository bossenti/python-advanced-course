# list creation
string_list = ["banana", "cherry", "apple"]
print(string_list)

empty_list = list()
print(empty_list)

# mixed data types and duplicates are allowed
mixed_list = [5, True, "apple", "apple"]

# access element
first_item = string_list[0]
last_ite = string_list[-1]

# iterate over list
for i in string_list:
    print(i)

# check item is in list
if "banana" in string_list:
    print("yes")
else:
    print("no")

# check how many items are in list
print(len(string_list))

# append elements
string_list.append("lemon")

# insert item at specific position
string_list.insert(1, "blueberry")
print(string_list)

# remove element
string_list.remove("cherry")

# remove all elements
string_list.clear()

# reverse order
string_list.reverse()

# sort list
string_list.sort()
new_list = sorted(string_list)

# list with same elements
zeroes = [0] * 5
ones = [1] * 7

# concat two lists
numbers = zeroes + ones
print(numbers)

# access subpart of lists
zeroes = numbers[:5]
ones = numbers[5:]
print(zeroes, ones)

# slice only each second item
numbers = numbers[::2]
numbers = numbers[::-1]  # reversing
print(numbers)

# copy a list
original = ["banana", "cherry", "apple"]
copy = original.copy()
copy = list(original)
copy = original[:]

# list comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8]
a_squared = [i**2 for i in a]

