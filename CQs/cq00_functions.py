__author__ = "730743044"


def mimic(message: str) -> str:
    """Return the same message that was inputed."""
    return message


def main() -> None:
    "Print result of calling mimic, main function to pull everything together"
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
