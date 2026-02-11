for num in range(0, 11):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"Factorial of {num} = {fact}")
