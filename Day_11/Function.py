# Day 11: Function - 30 Days of python programming
# Exercises: Level 1
# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
import math

def add_two_numbers(n_1, n_2):
    total = sum(n_1, n_2)
    return total

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    area = math.pi * (r ** r)
    return area

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    n = 0
    for num in nums:
        if not isinstance(num, str):
            print(f"{num} is not an number!")
            continue
        n += num
    return n

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
month = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
user_month = input("Enter a month number 1-12: ")
seasons = [ "Winter", "Spring", "Summer", "Autumn" ]
def check_season(user_month):
    while not isinstance(user_month, (int, str)):
        print(f"{user_month} is not a valid number!")
        user_month = input("Enter a valid month number 1-12: ")

    while isinstance(user_month, str) and not user_month.isdigit():
        print(f"{user_month} is not a valid number!")
        user_month = input("Enter a valid month number 1-12: ")

    user_month = int(user_month)
    while user_month not in range(1, 13):
        print(f"There's no month {user_month} after {month[11]}!")
        user_month = int(input("Enter a valid month number 1-12: "))

    return f"The season in {month[user_month - 1]} is {seasons[user_month % 12 // 3]}"

# 6. Write a function called calculate_slope which return the slope of a linear equation
# - I'm the guy who has the problem with math and still learning pre-algebra
# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# - The same answer as the answer number 6

# 8. Declare a function named print_list. It takes a list as j parameter and it prints out each element of the list.
lst = []
def print_list(*element):
    lst = [j for j in element]
    return lst

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
lst = []
def reverse_list(*items):
    lst = [i for i in reversed(items)]
    return lst

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
lst = []
def capitalize_list_items(*items):
    lst = [cap.capitalize() for cap in items]
    return lst

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
lst = []
def add_item(*element):
    lst = [j for j in element]
    return lst

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
lst = []
def remove_item(element):
    for i in element:
        if element in i:
            lst.remove(element)
    return lst

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(*nums):
    total = sum(*nums)
    return total

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(*nums):
    total = 0
    for i in nums:
        if i % 2 == 0:
            continue
        total += i
    return total

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(*nums):
    total = 0
    for i in nums:
        if i % 2 != 0:
            continue
        total += i
    return total

## Exercises: level 2
# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(nums):
    even = 0
    odd = 0

    num_str = str(nums)
    for digit in num_str:
        if int(digit) % 2 == 0:
            even += 1
            return
        odd += 1
    return even, odd

nums = 12456789 # Dummy value
even, odd = evens_and_odds(nums)

# 2. Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not a prime number!")
            break
    return f"{num} is a prime number"

# 3. Write a functions which checks if all items are unique in the list.
def is_unique(lst):
    unique_list = []
    duplicate_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
        elif i not in duplicate_list:
            duplicate_list.append(i)
    for i in unique_list:
        print(i)

# 4. Write a function which checks if all the items of the list are of the same data type.
def is_same_data_type(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if type(lst[j]) == type(lst[i]):
                print(f"{lst[j]} and {lst[i]} are the same data type")

# 5. Go to the data folder and access the countries-data.py file.
# - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

