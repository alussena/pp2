#1
import math
def degrees(deg):
    return deg*(math.pi/180)

deg = float(input())
print(degrees(deg))

#2
import math
def trapezoid_area(height, base1, base2):
    return (base1 + base2) * height / 2

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
print("Expected Output:", trapezoid_area(height, base1, base2))

#3
import math
def polygon_area(n, length):
    return (n * length**2) / (4 * math.tan(math.pi / n))


n = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
print("The area of the polygon is: ", round(polygon_area(n, length)))


#4
import math
def parallelogram_area(base, height):
    return base * height


base = float(input("length of base: "))
height = float(input("Height of parallelogram: "))
print("Expected Output: ", parallelogram_area(base, height))