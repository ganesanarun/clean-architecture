def percentage_of_word(search: str, file: str) -> float:
    search = search.lower()
    content = open(file, "r").read()
    words = content.split()
    number_of_words = len(words)
    occurrences = 0
    for word in words:
        if word.lower() == search:
            occurrences += 1
    return occurrences / number_of_words


if __name__ == "__main__":
    import sys

    print(percentage_of_word(sys.argv[1], sys.argv[2]))
