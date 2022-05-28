import random


def book_name():
    """This function makes a random choice of book_name. Possible book_names are listed in a books.txt file"""
    with open("books.txt", "r", encoding="UTF-8") as inp:
        lines = inp.readlines()
    random_book = random.choice(lines).strip()
    return random_book


if __name__ == '__main__':
    print(book_name())
