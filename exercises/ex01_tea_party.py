"""Throwing a tea party"""

__author__: str = "730743044"


def main_planner(guests: int) -> None:
    """This combines all the functions together"""
    print("A Cozy Tea Party for", (guests), "People!")
    """I had to put commas so that the words would be on the same line"""
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    """I had to make the cost function a string because there was a space
      between the $ and the cost"""
    """I had to use the tea_bags and treats functions
    so that it would multiply the tea_count and treat_count values by 2 and 1.5"""


def tea_bags(people: int) -> int:
    """The number of tea bags corresponds with the number of guests"""
    return people * 2
    """I didn't multiply by 2 at first, so I was not getting the right numbers"""


def treats(people: int) -> int:
    """The number of treats needed for number of guests"""
    return int(tea_bags(people=people) * 1.5)
    """Because I didn't multiply by 2 in the tea_bags function,
    I multiplied by 3 at first"""
    """I had to put int because the return type is int"""
    """I had to put people=people so that it would return people=some number"""


def cost(tea_count: int, treat_count: int) -> float:
    """The total cost of tea and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
