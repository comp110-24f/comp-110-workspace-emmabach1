"""playing around with lists"""

# creating a list variable tht's initially empty
my_numbers: list[float] = []  # with literal
my_numbers: list[float] = list()  # with constructor

# let's add ("append" a value to end of list)
my_numbers.append(1.5)
print(my_numbers)

# make a list of numbers
game_points: list[int] = [102, 86, 94]
print(game_points)

# print(game_points[2])
# print(game_points[len(game_points) - 1])

game_points[1] = 72  # update value at index 1

# changing characters in str --> convert to list
my_name: str = "Emma"
name_as_list: list[str] = list(my_name)
name_as_list[3] = "y"
print(name_as_list)
