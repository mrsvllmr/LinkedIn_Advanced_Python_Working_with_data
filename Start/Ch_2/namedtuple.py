# Demonstrate the usage of namedtuple objects

import collections

# Python tuple:
# - ordered and unchangeable
# - no default values

# TODO: create a Point namedtuple
Point = collections.namedtuple("Point", "x y")
P1 = Point(10,20)
P2 = Point(30,40)
print(P1,P2)
# can now be addressed via names
print(P1.x, P1.y)

# TODO: use _replace to create a new instance
P1 = P1._replace(x=100)
print(P1)