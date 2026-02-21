# 1. FizzBuzz using FOR loops

# 1) FizzBuzz Rules
# 1. If a number is divisible by 3, print Fizz!
# 2. If a number is divisible by 5, print Buzz!
# 3. If a number is divisible by 3 and 5, print FizzBuzz!
# 4. Enable a user to select the starting number and finish number 
# 5. The solution must contain a for loop!


# ﻿ Project Clues
# 1. A function that produces a range of numbers could come in handy...
# 2. How well do you remember conditional statements?
# 3. An arithmetic operator that identifies a remainder of 0 could come in handy...
# 4. Think carefully about the order you put the rules...

start= int(input("Enter the start number "))
end = int(input("Enter the last number "))
for i in range (start,end):
    if(i%3==0 and i%5==0):
        print("FizzBuzz!")
    elif(i%3==0):
        print("Fizz!")
    elif(i%5==0):
        print("Buzz!")
    else:
        print(i)