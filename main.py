def get_num_words(content):
    words = content.split()
    num_words = len(words)
    return num_words


def count_characters(text):
    mydict = {}
    lowered = text.lower()
    for letter in lowered:
        if letter in mydict:
            mydict[letter] += 1
        else:
            mydict[letter] = 1
    return mydict


def sort_on(mydict):
    return mydict["num"]


def char_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        if char.isalpha():
            sorted_list.append({"letter": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        char_dict = count_characters(file_contents)
        sorted_list = char_dict_to_sorted_list(char_dict)
        num_chars = get_num_words(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_chars} words found in the document")
        for item in sorted_list:
            print(f"The {item['letter']} character was found {item['num']} times")
        print("--- End report ---")


main()
