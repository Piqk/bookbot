from stats import word_counter
from stats import organizer

def get_book_text():
    path = 'books/frankenstein.txt'
    with open(path) as f:
        contents = f.read()
    return contents

print('============ BOOKBOT ============')
print('Analyzing book found at books/frankenstein.txt...')
print('----------- Word Count ----------')
print(word_counter())
print('--------- Character Count -------')
data = organizer()
sorted_data = sorted(data, key=lambda x: list(x.values())[0], reverse=True)
for d in sorted_data:
    for key, value in d.items():
        print(f"{key}: {value}")
print('============= END ===============')

