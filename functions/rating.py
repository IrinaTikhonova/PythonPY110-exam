import random


def rating():
    """Rating generator"""
    return round(random.random()*5, 2)


if __name__ == '__main__':
    print(rating())
