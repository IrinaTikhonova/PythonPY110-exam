from functions import book_name, author, rating, price, year, isbn, pages

from conf import MODEL

from itertools import count

import json


def library_generator(pk=1):
    library = {}
    for _ in count(pk, 1):
        library["model"] = MODEL
        library["pk"] = pk
        library["fields"] = {"title": book_name.book_name(), "year": year.year(),
                             "pages": pages.pages(), "isbn": isbn.isbn_lib(),
                             "rating": rating.rating(), "price": price.price(),
                             "author": author.author()}
        yield library
    pk += 1

def main(pk=1):
    with open("Библиотека.json", "w", encoding="Utf-8") as out:
        library = library_generator()
        final_library = []
        for _ in range(100):
            final_library.append(next(library))
        json.dump(final_library, out, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print(main())