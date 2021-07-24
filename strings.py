# Strings: ordered, immutable, text representation

# creation
my_string = "Hello World"
my_string_snd = 'This is python!'
my_string_thrd = """and its.. 
                    great
                    """  # multi-line string

# access single characters of the string
char = my_string[2]
substring = my_string[:5]

# concatenate strings
result = my_string + " " + my_string_snd

# iterate over single letters
for l in my_string:
    print(l)

# check letter exists in string
if 'e' in my_string:
    print("yes")

# remove unnecessary whitespace
short = my_string.strip()

# convert cases
my_string.lower()
my_string.upper()

my_string.find('o')  # returns index of first appearance
my_string.count('e')  # count number of occurrence
my_string_frth = my_string.replace('World', 'Universe')

# convert string to list of words
my_list = my_string.split()  # default delimiter is space

# convert list of strings to string
new_string = ' '.join(my_list)

# string formatting
var = "Tom"
age = 27
height = 1.85
sentence_percent_formatting = "This is %s, %d, %.2f m tall" % (var, age, height)
sentence_format_formatting = "This is {}, {}, {:.2f} m tall".format(var, age, height)
sentence_f_formatting = f"This is {var}, {age}, {height} m tall"
