from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

__author__ = "730743044"

"""Import Concatentation and Coordinates"""

x: str = "123"
y: str = "abc"
# these are global variables

print(concat(x, y))  # runs the concat file
print(get_coords(x, y))  # runs the coordinates file
