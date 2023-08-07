# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
# d = collections.deque('abcdefg')
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print(len(d))

# TODO: deques can be iterated over
for item in d:
    print(item)

# TODO: manipulate items from either end
d.appendleft('x')
d.append('x')
print(d)

# TODO: use an index to get a particular item
print(d[1])

d.popleft()
d.pop()
print(d)

d.rotate(2)
print(d)