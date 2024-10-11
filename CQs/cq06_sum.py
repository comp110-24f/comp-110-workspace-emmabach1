"""Summing the elements of a list using different loops"""

__author__ = "730743044"


def w_sum(vals: list[float]) -> float:
    sum: float = 0.0
    # local variable that is used to sum all the floats
    index = 0
    while index < len(vals):
        sum += vals[index]
        index += 1
    # used to add each value in the list
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    # local variable that is used to sum all the floats
    for elem in vals:
        sum += elem
    # adds every element in the list together
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    # local variable that is used to sum all the floats
    for index in range(0, len(vals)):
        # loop starts at 0 and ends at the length of list
        sum += vals[index]
    # adds each value at each index in the list together
    return sum


print(w_sum([1.1, 0.9, 1.0]))
print(f_sum([1.1, 0.9, 1.0]))
print(f_range_sum([1.1, 0.9, 1.0]))
