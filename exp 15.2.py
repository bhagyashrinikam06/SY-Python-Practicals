import math

def circle_area(r):
    return math.pi * r * r

def rectangle_area(l, b):
    return l * b

print("1. Circle")
print("2. Rectangle")
ch = int(input("Enter choice: "))

if ch == 1:
    r = float(input("Enter radius: "))
    print("Area of Circle:", circle_area(r))
elif ch == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area of Rectangle:", rectangle_area(l, b))
else:
    print("Invalid choice")