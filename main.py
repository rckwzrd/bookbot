def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def get_word_count(text):
    return len(text.split())


def get_char_count(text):
    chars = {}
    text = text.lower()
    for c in text:
        if c.isalpha():
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return [{"char":k,"count":v} for k,v in chars.items()]


def sort_on(dict):
    return dict["char"]


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = sorted(get_char_count(text), key=sort_on)

    print(f"--- Begin report for {book_path} ---")
    print(f"word count = {word_count}\n")
    for char in char_count:
        print(f"The {char['char']} was found {char['count']} times")
    print("--- End report ---")
    
main()
