from faker import Faker

fake = Faker()


# def isbn_lib():
#     return fake.numerify(text='%%%-%-%%%%%-%%%-%')
#
# print(isbn_lib())

def isbn_lib():
    return fake.isbn13(separator="-")


if __name__ == '__main__':
    print(isbn_lib())
