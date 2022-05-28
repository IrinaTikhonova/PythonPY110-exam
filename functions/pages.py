from random import randint


def pages():
    """Generates quantity of pages in books"""
    qty_of_pages = randint(10, 1000)
    return qty_of_pages


if __name__ == '__main__':
    print(pages())
