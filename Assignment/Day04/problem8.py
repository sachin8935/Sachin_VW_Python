start= int(input("Enter the start number "))
end = int(input("Enter the last number "))
while(start!=end):
    if(start%3==0 and start%5==0):
        print("FizzBuzz!")
    elif(start%3==0):
        print("Fizz!")
    elif(start%5==0):
        print("Buzz!")
    else:
        print(start)
start+=1
