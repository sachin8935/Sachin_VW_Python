#area of rectangle and permiter of rectangle
def area_of_rectangle(length, width):
    return length*width
def perimeter_of_rectangle(length, width):
    return 2*(length+width)

length = int(input("enter the length "))
width = int(input("enter the width "))

print(area_of_rectangle(length,width))
print(perimeter_of_rectangle(length,width))