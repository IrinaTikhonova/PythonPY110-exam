from faker import Faker
import random

fake = Faker()


def author():
    list_of_authors = []
    for _ in range(random.randint(1, 3)):
        list_of_authors.append(fake.name())
    return list_of_authors


if __name__ == '__main__':
    print(author())
