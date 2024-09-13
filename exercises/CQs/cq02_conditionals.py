__author__ = "730743044"


def guess_a_number() -> None:
    # this function will ask the user to guess the number
    # and take it as an input and print it back
    secret: int = 7
    x = input("Guess a number.")
    print("Your guess was " + str(x))
    # x has to be a str in order to print!

    if int(x) == secret:
        print("You got it!")
        # x has to be an int because secret is an int
    elif int(x) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
        # if x is less than secret it'll print the guess is too low
    else:
        print("Your guess was too high! The secret number is " + str(secret))
        # if x is bigger than secret it'll print the guess is too high


if __name__ == "__main__":
    guess_a_number()
# calling the main function
