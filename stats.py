def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents
    

def main():
    path = 'books/frankenstein.txt'
    result = get_book_text(path)
    return (result)