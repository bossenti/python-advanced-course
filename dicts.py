# dictionary: collection data type, unordered, mutable, key-value pairs

mydict = {"name": "Max", "age": 25, "city": "Berlin"}
mydict2 = dict(name="Finn", age=23, city="Stuttgart")

# accessing values
name = mydict["name"]

# add key-value pair
mydict["email"] = "max@forrest.com"

# delete items
del mydict["email"]
mydict.pop("age")
mydict.popitem()  # removes last inserted item

# check key is presence
if "name" in mydict2:
    print(mydict2["name"])
try:
    print(mydict2["age"])
except KeyError:
    print("Error")

# loop over keys
for key in mydict:
    print(key)
for key in mydict.keys():
    print(key)

# loop over values
for value in mydict.values():
    print(value)

# loop over both
for k, v in mydict.items():
    print(k, v)

# copy dict
copied_dict = mydict2.copy()  # dict(mydict2)

# merge two dictionaries (overwrites existing keys)
mydict.update(mydict2)

# possible key times are also number or tuples (or any immutable type)
number_dict = {1: 1, 2: 1, 3: 2, 4: 3, 5: 5}
tuple_dict = {(8, 7): 15}
