# Author: Nolan (AMDG) 10/12/2021

p = int(input("Enter the principal investment:  "))
r = float(input("Enter the annual intrest rate (as a decimal):  "))
n = 12
t = int(input("Enter the amount of time the money is invested(in years): "))

r /= 100

a = (p * (1 + (r / n)) ** (n * t))
print("is your future value" + str(a))