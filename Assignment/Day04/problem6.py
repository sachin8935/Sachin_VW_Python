text = """Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation. 
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, 
including structured, object-oriented and functional programming."""

text = text.lower()

letter_count = {}

for ch in text:
    if ch.isalpha():
        if ch in letter_count:
            letter_count[ch] += 1
        else:
            letter_count[ch] = 1

for key in sorted(letter_count):
    print(key, ":", letter_count[key])
