# Input a string from user and display unique characters in it. Hint: list(str) convert string to list of chars
str = input("Enter the paragraph")
arr= list(str)
result={}
for val in arr:
    if(val in result):
        result[val]+=1
    else:
        result[val]=1
print(result)

for (key,val) in result.items():
    if(val==1):
        print(f'the character {key} has count {val}')