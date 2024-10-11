"""list utility functions"""

__author__ = "730743044"


def all(input: list[int], value: int) -> bool:
    """Sees if all numbers in a list are equal to the value inputted"""
    if len(input) == 0:
        return False
    # if the list is empty it will return false
    for elem in input:
        if elem != value:
            return False
    # it will also return false if there is any number in the list
    # that is not the value inputted
    return True
    # returns true if all numbers in the list equal the value inputted


def max(input: list[int]) -> int:
    """Finds the largest number in the list"""
    if len(input) == 0:
        # if the list is empty it returns a value error
        raise ValueError("max() arg is an empty List")
    list_max = input[0]
    # local variable that represents the max value of the list
    for elem in input:
        if elem > list_max:
            list_max = elem
    # the max changes if one number in the list is bigger than the other
    return list_max


def is_equal(input_1: list[int], input_2: list[int]) -> bool:
    """Sees if the two lists are the same"""
    if len(input_1) != len(input_2):
        # in order for every element to be equal at every index, they must be same length
        return False
    for i in range(0, len(input_1)):
        if input_1[i] != input_2[i]:
            return False
    return True


def extend(input_1: list[int], input_2: list[int]) -> None:
    """Adds every value from the second list to the first"""
    for elem in input_2:
        input_1.append(elem)
    # adds values to the first list
