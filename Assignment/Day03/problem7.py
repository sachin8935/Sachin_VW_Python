def filter_long_words(words, length):
    result = []
    for word in words:
        if len(word) > length:
            result.append(word)
    return result

words = input("Enter words separated by space: ").split()
length = int(input("Enter length: "))

print(filter_long_words(words, length))
