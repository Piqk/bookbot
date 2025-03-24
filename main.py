from stats import main

def num_words():
    book = main()
    first_step = book.split()
    number = 0
    for word in first_step:
        number += 1
    print (f"{number} words found in the document")


num_words()
    



