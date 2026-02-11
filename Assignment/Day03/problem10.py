tup = tuple(map(int, input("Enter tuple elements: ").split()))
value = int(input("Enter value to find: "))

count = tup.count(value)

if count > 1:
    print(value, "is repeated", count, "times")
elif count == 1:
    print(value, "is not repeated")
else:
    print(value, "not found in tuple")
