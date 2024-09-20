"""EXO2 - Chardle - A cute step toward Wordle."""

__author__ = "730743044"


def input_word() -> str:
    """Word that user inputs"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:  # word doesn't return if it is not 5 characters and ends code
        print("Error: Word must contain 5 characters.")
        exit()
    return word  # word will return if it is 5 characters


def input_letter() -> str:
    """Letter that user inputs"""
    letter: str = input("Enter a single character: ")
    if (
        len(letter) != 1
    ):  # if the word's length doesn't equal 1, it prints error and ends code
        print("Error: Character must be a single character.")
        exit()
    return letter  # returns if length of letter is 1


def contains_char(word: str, letter: str) -> None:
    """Finds if letter is in word and how many times"""
    print("Searching for " + letter + " in " + word)
    x = 0  # x is the number of matching letters

    if word[0] == letter:
        print(letter + " found at index 0")
        x += 1

    if word[1] == letter:
        print(letter + " found at index 1")
        x += 1

    if word[2] == letter:
        print(letter + " found at index 2")
        x += 1

    if word[3] == letter:
        print(letter + " found at index 3")
        x += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        x += 1
    if x == 0:
        print("No instances of " + letter + " found in " + word)
        # if the letter is not in the word
    elif x == 1:
        print(str(x) + " instance of " + letter + " found in " + word)
        # if the letter is found once in the word
    else:
        print(str(x) + " instances of " + letter + " found in " + word)
        # if the letter is in the word x amount of times


def main() -> None:
    """Calls all the functions"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
