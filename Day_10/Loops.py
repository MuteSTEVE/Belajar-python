# Day 10: Loops - 30 Days of python programming
# Exercises: Level 1
# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(10):
    i += 1
    print(i)
print("-----------------------------------")

n = 0
while n < 10:
    n += 1
    print(n)
print("-----------------------------------")

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, 0, -1):
    i -= 1
    print(i)
print("-----------------------------------")

n = 10
while n > 0:
    n -= 1
    print(n)
print("-----------------------------------")

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
for i in range(7):
    for j in range(i+1):
        print('#', end='')
    print()
print("-----------------------------------")

# 4. Use nested loops to create the following:
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
for i in range(7):
    for j in range(7):
        print('#', end=' ')
    print()
print("-----------------------------------")

# 5. Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for i in range(-1, 10):
    i += 1
    print(f'{i} x {i} = {i * i}')
print("-----------------------------------")

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)
print("-----------------------------------")

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(100):
    i += 1
    if i % 2 != 0:
        continue
    print(i)
print("-----------------------------------")

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(100):
    i += 1
    if i % 2 == 0:
        continue
    print(i)
print("-----------------------------------")

## Exercises: Level 2
# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# Example: The sum of all numbers is 5050.
n = 0
for i in range(100):
    n += i
print(f"The sum of all numbers is: {n}")
print("-----------------------------------")

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# Example: The sum of all evens is 2550. And the sum of all odds is 2500.
n = 0
for i in range(100):
    if i % 2 != 0:
        continue
    n += i
print(f"The sum of all even numbers is: {n}")

n = 0
for i in range(100):
    if i % 2 == 0:
        continue
    n += i
print(f"The sum of all odd numbers is: {n}")
print("-----------------------------------")

### Exercises: Level 3
countries = [ 'Afghanistan'   'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe' ]

# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
for country in countries:
    if 'land' in country:
        print(country)
print("-----------------------------------")

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
for i in reversed(fruits):
    print(i)
print("-----------------------------------")
