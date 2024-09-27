"""Concats words together"""

__author__ = "730743044"


def concat(word1: str, word2: str) -> str:
    return word1 + word2  # this combines the words together


if __name__ == "__main__":  # so it doesn't print in visualize.py
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
