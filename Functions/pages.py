from random import randint


def pages():
    qty_of_pages = randint(10, 1000)
    return qty_of_pages


if __name__ == '__main__':
    print(pages())
