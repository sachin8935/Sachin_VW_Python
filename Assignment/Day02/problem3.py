n= input("Enter a four digit number ")
if(len(n)!=4):
    print("please enter 4 digit number only")
else:
    n = int(n)
    fourth_digit= n%10
    third_digit= (n//10)%10
    second_digit= (n//100)%10
    first_digit= (n//1000)%10
    print(f"{first_digit} {second_digit} {third_digit} {fourth_digit}")
    place=1
    number =0
    while(n!=0):
        temp = n%10
        n=n//10
        number = (number*10) +temp
        print(temp*place)
        place*=10
    print(number)