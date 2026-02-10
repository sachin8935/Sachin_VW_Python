num = int(input("Enter a 4-digit number: "))

thousands = num // 1000
hundreds = (num // 100) % 10
tens = (num // 10) % 10
ones = num % 10

print("\nFace values:")
print(thousands, hundreds, tens, ones)

print("\nPlace values:")
print(thousands * 1000, hundreds * 100, tens * 10, ones * 1)

reverse_num = (ones * 1000) + (tens * 100) + (hundreds * 10) + (thousands * 1)

print("\nReversed number:", reverse_num)
