import shelve

books = shelve.open("book")
books["recipes"] = {
    "blt": ["bacon", "lettuce", "tomato", "bread"],
    "beans_on_toast": ["beans", "bread"],
    "scrambled_eggs": ["eggs", "butter", "milk"],
    "soup": ["tin_of_soup"],
    "pasta": ["pasta", "cheese"]
}
books["maintenance"] = {
    "stuck": ["oil"],
    "loose": ["gaffer_tape"]
}

print(books["recipes"])
# print(books["recipes"]["scrambled_eggs"])
#
# print(books["maintenance"]["loose"])
books.close()
