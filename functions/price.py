import random


def price():
    """Book prices generator"""
    return round(random.uniform(100, 1000), 2)


if __name__ == '__main__':
    print(price())
