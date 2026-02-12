s = input("Enter a string: ")
chars = list(s)

unique_chars = []
for ch in chars:
    if ch not in unique_chars:
        unique_chars.append(ch)

print("Unique characters:", unique_chars)
