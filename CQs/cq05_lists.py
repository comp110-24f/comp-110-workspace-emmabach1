"""Mutating functions."""

__author__ = "730743044"


def manual_append(list: list[int], value: int) -> None:
    list.append(value)

# adds the inputted value to the list


def double(list: list[int]) -> None:
    index = 0
    while index < len(list):
        list[index] *= 2
        index += 1


# multiplies each value in the list by 2

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
# these are global variables


double(list_2)
print("list_1: ", list_1)
print("list_2: ", list_2)

# list_1 and list_2 will print the same thing
# since we defined list_1 equal to list_2
