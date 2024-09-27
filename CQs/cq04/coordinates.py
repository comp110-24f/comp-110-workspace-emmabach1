"""Forming coordinates"""

__author__ = "730743044"


def get_coords(xs: str, ys: str) -> None:
    """Each character of the string becomes coordinates"""
    index = 0
    while index < len(xs):
        index1 = 0
        while index1 < len(ys):
            # while loop will run when first while loop is true
            print("(" + xs[index] + "," + ys[index1] + ")")
            index1 += 1  # this increases the y index by 1
        index += 1  # this increases the x index by 1


# will print the first xs index with different ys indexes until ys loop is false
# xs index will increase by one and print with next y indexes until ys loop is false
# loops until xs while loop is false
