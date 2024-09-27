"""Using a while loop to iterate over a string"""

__author__ = "730743044"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # the number of characters that are the same in the phrase
    index: int = 0  # the place of the letter in the phrase
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
            index = index + 1
            print(count)
        else:
            index = index + 1
    return count


# if the index is less than the length of phrase
# and if the letter at the index is the same as what we typed
# the count will increase by one
# the code will do this for each index position until it counts the
# number of same characters there are


num_instances(phrase="Bobby", search_char="o")
