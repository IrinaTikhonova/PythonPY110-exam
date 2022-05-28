from random import randint


def year():
    """Year of book issue"""
    book_year = randint(1600, 2022)
    return book_year


if __name__ == '__main__':
    print(year())
