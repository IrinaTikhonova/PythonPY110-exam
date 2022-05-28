import random


def book_name():
    with open("books.txt", "r", encoding="UTF-8") as inp:
        lines = inp.readlines()
    random_book = random.choice(lines).strip()
    return random_book


if __name__ == '__main__':
    print(book_name())
