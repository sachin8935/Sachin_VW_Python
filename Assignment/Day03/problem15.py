num = [2, 3, 4, 5, 2, 6, 3, 2]
result = []

for item in num:
    if item not in result:
        result.append(item)

print("Result:", result)
