# some advanced iterable tools

# product
# computes the cartesian product
from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b, repeat=2)  # optional: number of repetitions
print(list(prod))

# permutation
# return all possible orderings
from itertools import permutations

a = [1, 2, 3]
perm = permutations(a, 2)  # optional parameter for length (2)
print(list(perm))

# combination
# return all possible combinations of a certain length
from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_w_r = combinations_with_replacement(a, 2)
print(list(comb_w_r))

# accumulate
# returns accumulate sums, or of other functions
from itertools import accumulate
import operator

a = [1, 2, 3, 4]
acc_sum = accumulate(a)
acc_prod = accumulate(a, func=operator.mul)
print(list(acc_sum))
print(list(acc_prod))

# groupby
# iterator that returns keys and groups of the input
from itertools import groupby


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)  # lambdas can be used as well
for k, v in group_obj:
    print(k, list(v))

# infinite iterators

from itertools import count, cycle, repeat

for i in count(10):  # infinite loop that starts at 10
    print(i)
    if i == 20:
        break

a = [1, 2, 3]
for i in cycle(a):  # infinite loop tha cycles through a
    break

for i in repeat(1):  # infinite loop repeating the given value
    break
