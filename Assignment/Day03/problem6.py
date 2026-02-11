lst = list(map(int, input("Enter list elements: ").split()))

largest = lst[0]
for num in lst:
    if num > largest:
        largest = num

print("Largest number:", largest)
