# 4) Random Password Generator (Console App)

# The objective of this program is to generate a secure password using random characters and display it to the user through a console interface.

# # Requirements:
# - The program should generate a password consisting of:
#   - Random uppercase letters (A–Z)
#   - Random lowercase letters (a–z)
#   - Random digits (0–9)
#   - Random special characters (e.g., `!@#$%^&*`)
# - The password length should be fixed (e.g., 8–12 characters) or configurable by the user.
# - The generated password must be:
#   - Randomized  and unique each time the program runs.
#   - Displayed clearly on the console (UI).
# - The program should ensure that the password contains a mix of all character types for better security.
import random
lowercase="abcdefghijklmnopqrstuvwxyz"
uppercase= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num= "1234567890"
special="!@#$%^&*"
print("Enter 1 if you want the password to be 8-12 digits")
print("Enter 2 if you want password to be of length of your choice")
choice=int(input("Enter your choice "))
result=""
if(choice==1):
    digit = random.randint(8,12)
    each_digit= digit//4
    print(each_digit)
    for i in range (0,each_digit):
        result+=random.choice(lowercase)
        result+=random.choice(uppercase)
        result+=random.choice(num)
        result+=random.choice(special)
    for i in range (0,digit%4):
        result+=random.choice(special)
    print(result)
if(choice==2):
    digit = int(input("Enter the digit of password required "))
    each_digit= digit//4
    for i in range (0,each_digit):
        result+=random.choice(lowercase)
        result+=random.choice(uppercase)
        result+=random.choice(num)
        result+=random.choice(special)
    for i in range (0,digit%4):
        result+=random.choice(special)
    print(result)
    
