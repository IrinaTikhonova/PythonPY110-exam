from Functions import book_name, author, rating, price, year, isbn, pages

from Functions.conf import MODEL

from itertools import count

import json

def library_generator(pk=1):
    library = {}
    for _ in count(pk,1):
        library["model"] = MODEL
        library["pk"] = pk
        library["fields"] = {"title":book_name.book_name(), "year": year.year(),
                             "pages": pages.pages(), "isbn": isbn.isbn_lib(),
                             "rating": rating.rating(),"price": price.price(),
                             "author": author.author()}
        yield library
        pk +=1



library = library_generator()
with open("Библиотека.txt", "w", encoding="utf-8") as out:
    for _ in range(100):
        json.dump(next(library), out, indent=4)

