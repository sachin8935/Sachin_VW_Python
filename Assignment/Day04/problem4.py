converters = [
    lambda t: t * 1000,          
    lambda kg: kg * 1000,        
    lambda g: g * 1000,          
    lambda mg: mg * 0.00000220462  
]

tonns = float(input("Enter weight in tonns: "))

kg = converters[0](tonns)
gm = converters[1](kg)
mg = converters[2](gm)
lbs = converters[3](mg)

print("Kilograms:", kg)
print("Grams:", gm)
print("Milligrams:", mg)
print("Pounds:", lbs)
