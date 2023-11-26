# Day 2: 30 Days of python programming
import math

# Exercise 1-13 level1
name, last, full, country, city, age, year, Is_married, Is_true, Is_light_on = "Satrio", "Baharudin", "Satrio Baharudin", "Indonesia", "Jakarta", 18, 2023, False, True, True
# Exercise 1 level2
print(f"name = {name}{type(name)}")
print(f"last = {last}{type(last)}")
print(f"full = {full}{type(full)}")
print(f"country = {country}{type(country)}")
print(f"city = {city}{type(city)}")
print(f"age = {age}{type(age)}")
print(f"year = {year}{type(year)}")
print(f"Is_married = {Is_married}{type(Is_married)}")
print(f"Is_true = {Is_true}{type(Is_true)}")
print(f"Is_light_on = {Is_light_on}{type(Is_light_on)}")

## Exercise 1 level 2
len_name = len(name)
len_last = len(last)
## Exercise 3 level 2
if len_name < len_last:
    print("first name is shorter than last name")
elif len_name > len_last:
    print("first name is longer than last name")
else:
    print("first name and last name is the same")

## Exercise 4 level 2
num_one = 5
num_two = 4

total = num_one + num_two               # I
diff = num_one - num_two                # II
product = num_one * num_two             # III
division = num_one / num_two            # IV
remainder = num_one % num_two           # V
exp = num_one ** num_two                # VI
floor_division = num_one // num_two     #VII

## Exercise 5 level 2
radius = int(input("Input the radius of the circle: "))
area = math.pi * (radius ** 2)
print(f"The are of the circle is: {area}")                             # I

## Exercise 6 
name = str(input("Input your name: "))
last = str(input("Input your last name: "))
country = str(input("Input your your country: "))
age = int(input("Input your age: "))
print(f"Your name is: {name}")
print(f"Your last name is: {last}")
print(f"Your country is: {country}")
if age < 18:
    print("Your still a children")
elif age > 18:
    print("Your a teenager")
else:
    print("Idk")
