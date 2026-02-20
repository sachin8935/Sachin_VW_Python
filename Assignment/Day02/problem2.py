def farenheit_to_celcius(temprature):
    return ((temprature-32)*(5/9))
def celcius_to_farenheit(temprature):
    return (temprature*(9/5))+32

print("Enter 1 for fareneheit to celcius")
print("Enter 2 for celcisu to farehenit")
x= input("Enter your choice")
x= int(x)
if(x==1):
    temprature = input("Enter temprature in farenheit")
    temprature= int(temprature)
    print(farenheit_to_celcius(temprature))
else:
    temprature = input("Enter temprature in celcius")
    temprature= int(temprature)
    print(celcius_to_farenheit(temprature))