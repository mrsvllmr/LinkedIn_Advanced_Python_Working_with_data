# Demonstrate the usage of defaultdict objects

from collections import defaultdict


# define a list of items that we want to count
fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']

# # TODO: use a dictionary to count each element
# fruitCounter = dict()
#
# # TODO: Count the elements in the list
# for fruit in fruits:
#     if fruit in fruitCounter.keys():
#         fruitCounter[fruit] += 1
#     else:
#         fruitCounter[fruit] = 1
#
# # TODO: print the result
# print(fruitCounter)
#
# this solution works fine, but the following is easier (compare for loop)


# TODO: use a dictionary to count each element
fruitCounter = defaultdict(int)
# fruitCounter = defaultdict(lambda: 100)

# TODO: Count the elements in the list
for fruit in fruits:
    fruitCounter[fruit] += 1

# TODO: print the result
print(fruitCounter)