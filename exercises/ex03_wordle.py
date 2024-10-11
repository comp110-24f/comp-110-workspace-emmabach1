"""Wordle"""

__author__ = "730743044"


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    N: int = 1  # number of turns
    while N <= 6:  # there are 6 turns
        print(f"=== Turn {N}/6 ===")
        guess = input_guess(len(secret_word))
        # guess has to be the length of secret_word
        print(emojified(guess, secret_word))  # prints emoji results of user's guess
        if guess == secret_word:
            print(f"You won in {N}/6 turns!")
            # will replace N with a number, depending on what turn it is
            return
        N += 1
    print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_length: int) -> str:
    """Word that user inputs"""
    guess: str = input(f"Enter a {secret_length} character word: ")
    while len(guess) != secret_length:
        # will repeat until user enters the correct length word
        guess = input(f"That wasn't {secret_length} chars! Try again: ")
        # user will be prompted to input another word
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Sees if guess is in word"""
    assert len(char_guess) == 1  # char_guess must be 1 character
    index: int = 0
    char_word: bool = False  # created a local variable so that the bool will return
    while index < len(secret_word):  # will iterate over the length of secret_word
        if secret_word[index] == char_guess:
            char_word = True
        index += 1
    return char_word


def emojified(guess: str, secret_word: str) -> str:
    """Shows emojis that correspond to result"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emojis: str = ""  # this is an empty string initially
    while index < len(guess):  # will iterate over length of guess
        if guess[index] == secret_word[index]:
            emojis += GREEN_BOX  # adds emoji if character is in correct position
        elif contains_char(secret_word, guess[index]):
            emojis += YELLOW_BOX  # adds emoji if character is in word
            # but not in right position
        else:
            emojis += WHITE_BOX  # adds emoji if character is not in word
        index += 1
    return emojis


if __name__ == "__main__":
    main(secret_word="codes")
