# Day 9: Conditional - 30 Days of python programming
import random

# Exercises: Level 1
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
legal = 18
user = int(input('Enter your age: '))
if user >= legal:
    print('Congrats! You are old enough to drive')
else:
    print(f'Sorry buddy, you need {legal - user} more years to drive')
print('-----------------------------------')

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = random.randint(0, 30)
your_age = int(input('Enter your age: '))
def compareAge(my_age, your_age):
    if your_age > my_age:
        print(f'You were {your_age - my_age} years older than me')
        return

    if your_age < my_age:
        print(f'You were {my_age - your_age} years younger than me')
        return

    print(f'We both also {your_age} years old')
compareAge(my_age, your_age)
print('-----------------------------------')

# 3.  o numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
A = int(input('Enter number A: '))
B = int(input('Enter number B: '))
def compareVal(A, B):
    if A > B:
        print(f'{A} is greater than {B}')
        return

    if A < B:
        print(f'{A} is smaller than {B}')
        return

    print(f'{A} is equal to {B}')
compareVal(A, B)
print('-----------------------------------')

## Exercises: Level 2
# 1. Write a code which gives grade to students according to theirs scores:
scores = int(input('Enter your score: '))
def gradeScores(scores):
    if scores >= 80:
        print('Congrats! You got A')
        return

    if scores >= 70:
        print('Not bad, You got B')
        return

    if scores == 69:
        print('Noice scores XD')
        return

    if scores >= 60:
        print('You got C, Better luck next time!')
        return

    if scores >= 50:
        print('My goodness, study harder! you only got D')

    print('WT- F, you\'re playing too much videogame bruv!')
gradeScores(scores)
print('-----------------------------------')

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
user_month = int(input('Enter a month number 1-12: '))
def seasonMonth(user_month, month):
    if user_month <= 2 or user_month == 12:
        season = 'Winter'
        print(f'The season in {month[user_month]} is {season}')
        return

    if user_month <= 5:
        season = 'Spring'
        print(f'The season in {month[user_month]} is {season}')

        return
    if user_month <= 8:
        season = 'Summer'
        print(f'The season in {month[user_month]} is {season}')
        return

    if user_month <= 11:
        season = 'Autumn'
        print(f'The season in {month[user_month]} is {season}')
        return

    print(f'There are no month {user_month}!')
seasonMonth(user_month, month)
print('-----------------------------------')

# 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
user_fruit = input('Enter a fruit name: ')
if user_fruit not in fruits:
    fruits.append(user_fruit)
    print(fruits)
else:
    print(f'{user_fruit} already exist in the list')
print('-----------------------------------')

# 4. Here we have a person dictionary. Feel free to modify it!
person = {
        'first_name': 'Walter',
        'last_name': 'White',
        'age': 50,
        'country': 'USA',
        'is_marred': 1,
        'skills': ['Chemistry', 'Money laundering', 'Mathematic', 'Balling', 'JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address':{
            'House': 308,
            'Street': 'Negra Arroyo Lane',
            'City': 'Albuquerque',
            'State': 'New Mexico',
            'ZipCode': 87104
            }
        }

# - Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
def personSkills(person):
    first_name = person.get('first_name')
    if 'skills' not in person:
        print(f'{first_name} doesn\'t have skills')
        return

    skills_lt = person.get('skills')
    if not skills_lt:
        print(f'{first_name} skills are empty')
        return

    mid_len = len(skills_lt) // 2
    mid = skills_lt[mid_len]
    if len(skills_lt) % 2 == 0:
        mid_len_2 = mid_len - 1
        mid_2 = skills_lt[mid_len_2]
        mid_val = [mid_2, mid]
        print(mid_val)
        return

    print(mid)
personSkills(person)
print('-----------------------------------')

# - Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
def pythonSkills(person):
    first_name = person.get('first_name')
    if 'skills' not in person:
        print(f'{first_name} doesn\'t have skills')
        return

    skills_lt = person.get('skills')
    if not skills_lt:
        print(f'{first_name} skills are empty')
        return

    if 'Python' not in skills_lt:
        print(f'{first_name} doesn\'t have python skills')
        return

    print(skills_lt)
pythonSkills(person)
print('-----------------------------------')

# - If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# "more conditions can be nested"
# Guard clauses: 'I don't think i will'
def devSkills(person):
    skills_lt = person.get('skills')
    if 'React' and 'JavaScript' in skills_lt:
        print('He is a front end developer')
        return

    if 'Node' and 'Python' and 'MongoDB' in skills_lt:
        print('He is a backend developer')
        return

    if 'React' and 'Node' and 'MongoDB' in skills_lt:
        print('He is a fullstack developer')
        return

    print('unknown title')
devSkills(person)

# - If the person is married and if he lives in Country, print the information in the following format example:
# Asabeneh Yetayeh lives in Finland. He is married.
def personStatus(person):
    first_name = person.get('first_name')
    last_name = person.get('last_name')
    country = person.get('country')
    married = person.get('is_married')
    if 'country' in person and married == 1:
        print(f'{first_name} {last_name} lives in {country} and He is married')
        return

    if 'country' in person and 'married' not in person:
        print(f'{first_name} {last_name} lives in {country}')
        return

    if 'country' in person and married == 0:
        print(f'{first_name} {last_name} lives in {country}')
        return

    if married == 1 and 'country' not in person:
        print(f'{first_name} {last_name} is married')
        return

    print(f'Where\'s {first_name} {last_name} live and is he married?')
personStatus(person)
