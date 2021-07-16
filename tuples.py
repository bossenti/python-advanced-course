# Tuple: collection data type, that is ordered,immutable (in contrast to a list), allows duplicate elements
# often used for objects that belong together

# create a tuple
my_tuple = ("Max", 28, "Boston")  # parenthesis are optional
single_element_tuple = ("Max",)
my_tuple = tuple(["Max", 28, "Boston"])  # create tuple from iterable

# access item
item = my_tuple[1]

# iterate over tuple
for x in my_tuple:
    print(x)

# number of elements
print(len(my_tuple))

# count elements
print(my_tuple.count("Max"))

# find first index of occurrence
print(my_tuple.index(28))

# conversion to list (works in both directions)
my_list = list(my_tuple)

# access sub-parts (slicing, same as for lists)
age, location = my_tuple[1:]

# unpacking
my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple  # +i2 contains all elements between in a list

# working with tuples can be more efficient than lists (tuples use less memory)
