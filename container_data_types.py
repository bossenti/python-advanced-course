# collections: special container data types with additional functionalities compared to lists, tuples, etc.

# counter
# stores elements (keys) and their frequency counts (values) as a dictionary
from collections import Counter

test_string = "aaaaaaaabbaaaccc"
my_counter = Counter(test_string)  # use any iterable (list etc.)
print(my_counter)
print(my_counter.most_common(1))  # most common element(s)

# namedtuple
# lightweight object type
from collections import namedtuple

Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt.x)

# OrderedDict
# dictionary that remembers the order of insertion (like usual dicts >= Python 3.7)
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['c'] = 3
ordered_dict['b'] = 2
ordered_dict['d'] = 4
print(ordered_dict)

# defaultdict
# returns default value of the specified default type when a key is empty
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])

# deque
# double ended queue, add and remove elements from both ends (efficiently)
from collections import deque
d = deque()

d.append(1)
d.append(2)
print(d)

d.appendleft(0)
print(d)

d.pop()
d.popleft()
print(d)

d.rotate(1)  # rotates all elements one place to the right (to rotate to the left use negative numbers)

