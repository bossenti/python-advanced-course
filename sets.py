# Set: collection data-type, unordered, mutable, no duplicates

# creation
my_set = {1, 2, 3}
my_set_2 = set([1, 2, 3])
my_set_3 = set("Hello")  # good trick to count number of different characters in one word

# empty set
empty_set = set  # {} creates a dictionary

# add elements
my_set.add(4)

# remove elements
my_set.remove(3)
my_set.discard(2)  # does not throw an error if element does not exist

# remove all elements
my_set_3.clear()

# iterate over set
for i in my_set:
    print(i)

# check element is in set
if 1 in my_set:
    print("Yes")

# combine elements from both sets
union = my_set.union(my_set_2)

# only elements that are in both sets
intersec = my_set.intersection(my_set_2)

# determine the difference of two sets
diff = my_set.difference(my_set_2)

# all elements that are in one of set but not in both
sym_diff = my_set.symmetric_difference(my_set_2)

# check set is a subset of the other other
print(my_set.issubset(my_set_2))

# check set is a superset of the other
print(my_set.issuperset(my_set_2))

# check for same elements
print(my_set.isdisjoint(my_set_2))

# immutable set
a = frozenset([1, 2, 3, 4])
