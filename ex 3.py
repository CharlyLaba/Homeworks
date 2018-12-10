import math

radius_input = input("Please enter a radius: ")
to_float = float(radius_input)

area_eq= math.pi*pow(to_float,2)

print("The Area of your Circle is: " + str(area_eq))