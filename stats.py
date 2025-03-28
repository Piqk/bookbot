def get_book_text():
    path = 'books/frankenstein.txt'
    with open(path) as f:
        contents = f.read()
    return contents

def word_counter():
    counter = 0
    for i in get_book_text().split():
        counter += 1 
    return (f'Found {counter} total words')

book = str(get_book_text())

def count_char():
    pairs = {}
    for i in book.lower():
        if i not in pairs:
            n = 1
            pairs.update({i: n})
        elif i in pairs:
            pairs[i] += 1
    return pairs





def organizer():
    list_of_dict = [{k: v} for k, v in count_char().items()]
    data = sorted(list_of_dict, key=lambda d: next(iter(d.values())), reverse=True)
    return (data)





   


             


