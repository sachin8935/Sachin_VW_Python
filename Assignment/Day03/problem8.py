quantity = int(input("Enter quantity: "))
unit_price = 5

total_price = quantity * unit_price

if quantity > 50:
    discount = 0.15
elif quantity > 30:
    discount = 0.10
else:
    discount = 0

final_price = total_price - (total_price * discount)

print("Total price after discount: Rs", final_price)
