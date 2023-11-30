# Day 3: 30 Days of python programming
import math

# Exercise 1
# 1. Declare your age as integer variable
age = 18
print(f"Your age is: {age}")
print("-----------------------------------")

# Exercise 2
# 2. Declare your height as a float variable
height = float(173)
print(f"Your height is: {200}cm")
print("-----------------------------------")

#  Exercise 3
# 3. Declare a variable that store a complex number
comp = 18 + 173j
print(f"The complex number is: {comp}")
print("-----------------------------------")

# Exercise 4
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = int(input("Enter the base: "))
h = int(input("Enter the height: "))
area_of_triangle = ((1/2) * b * h)
print(f"The are of the triangle is: {area_of_triangle}")
print("-----------------------------------")

# Exercise 5
# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter_of_triangle = (a + b + c)
print(f"The perimeter of the triangle is: {perimeter_of_triangle}")
print("-----------------------------------")

# Exercise 6
# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter length: "))
width = int(input("Enter length: "))
area_of_rectangle = 2 * (length + width)
print(f"The area of the rectangle is: {area_of_rectangle}")
print("-----------------------------------")

# Exercise 7
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("Enter radius: "))
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = math.pi * 2 * radius
print(f"The area of the circle is: {area_of_circle}")
print(f"The circum of the circle is: {circum_of_circle}")
print("-----------------------------------")

# Exercise 8
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Exercise 9
# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Exercise 10
# 10. Compare the slopes in tasks 8 and 9.
# Exercise 11
# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# Exercise 12
# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python = "python"
dragon = "dragon"
if len(python) != len(dragon):
    print("Python is not the same as dragon")
else:
    print("Python is the same as dragon")
print("-----------------------------------")

# Exercise 13
# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
if "on" in python and dragon:
    print(f"Found 'on' in {python} and {dragon}")
else:
    print("Not found")
print("-----------------------------------")

# Exercise 14
# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
text_jargon = "I hope this course is not full of jargon"
if "jargon" in text_jargon:
    print(f"Found 'jargon' in {text_jargon}")
else:
    print("Not found")
print("-----------------------------------")

# Exercise 15
# 15. There is no 'on' in both dragon and python

# Exercise 16
# 16. Find the length of the text python and convert the value to float and convert it to string
python_text = "python"
python_float = float(len(python_text))
python_string = str(python_float)
print(f"Float of length python: {python_float}")
print(f"String of float-ength python: {python_string}")
print("-----------------------------------")

# Exercise 17
# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num_check = int(input("Enter the number: "))
if num_check % 2 == 0:
    print(f"{num_check} is even number")
else:
    print(f"{num_check} is odd number")
print("-----------------------------------")

# Exercise 18
# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
int_val = int(2.7)
if floor_division == int_val:
    print("It's equal")
else:
    print("It's not equal")
print("-----------------------------------")

# Exercise 19
# 19. Check if type of '10' is equal to type of 10
val_1 = '10'
val_2 = 10
if type(val_1) == type(val_2):
    print(f"The type of {val_1} and {val_2} are equal")
else:
    print("The type are not equal")
print("-----------------------------------")

# Exercise 20
# 20. Check if int('9.8') is equal to 10
# This Exercise is dumb and will produce an error

# Exercise 21
# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))
pay = int(input("Enter pay per hour: "))
earning = hours * pay
print(f"The earning that you got is ${earning}")
print("-----------------------------------")

# Exercise 22
# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
syear = int(input("Enter your age: "))
year_to_seconds = 31557600
hundred_years = syear * year_to_seconds
print(f"You've been lived for {hundred_years} seconds")
print("-----------------------------------")
