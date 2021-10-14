# Author: Nolan (AMDG) 10/12/2021

x_one = int(input("Input x1 point: "))
y_one = int(input("Input y1 point: "))
x_two = int(input("Input x2 point: "))
y_two = int(input("Input y2 point: "))

cord_1 = (x_two - x_one) ** 2
cord_2 = (y_two - y_one) ** 2

d = cord_1 + cord_2

distance = d ** (1/2)
print("The distance between the two points is " + str(distance))
