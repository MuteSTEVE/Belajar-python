# Day 5: 30 Days of python programming
# Exercise 1
# 1. Declare an empty list
empty = []
print("-----------------------------------")

# Exercise 2
# 2. Declare a list with more than 5 items
fruits = [ 'banana', 'mango', 'orange', 'lemon', 'strawberry', 'melon' ]
print("-----------------------------------")

# Exercise 3
# 3. Find the length of your list
print(f"The length of the fruits is {len(fruits)}")
print("-----------------------------------")

# Exercise 4
# 4. Get the first item, the middle item and the last item of the list
first = fruits[0]
last = fruits[-1]
mid_len = len(fruits) // 2 - 1
mid = fruits[mid_len]
if len(fruits) % 2 == 0:
    mid_2_id = mid_len + 1
    mid_2 = fruits[mid_2_id]
    print(f"The first fruit: {first}\nthe middle fruit: {mid} and {mid_2}\nand the last fruit: {last}")
else:
    print(f"The first fruit: {first}\nthe middle fruit: {mid}\nand the last fruit: {last}")
print("-----------------------------------")

# Exercise 5
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = [ 'Satrio', 18, 172, False, 'Pik blok D no 64']

# Exercise 6
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = [ 'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon' ]

# Exercise 7
# 7. Print the list using print()
print(f"IT companies: {it_companies}")
print("-----------------------------------")

# Exercise 8
# 8. Print the number of companies in the list
print(f"The total number of IT companies: {len(it_companies)}")
print("-----------------------------------")

# Exercise 9
# 9. Print the first, middle and last company
first = it_companies[0]
last = it_companies[-1]
mid_len = len(it_companies) // 2 - 1
mid = it_companies[mid_len]
if len(it_companies) % 2 == 0:
    mid_2_id = mid_len + 1
    mid_2 = it_companies[mid_2_id]
    print(f"The first company: {first}\nthe middle company: {mid} and {mid_2}\nand the last company: {last}")
else:
    print(f"The first company: {first}\nthe middle company: {mid}\nand the last company: {last}")
print("-----------------------------------")

# Exercise 10
# 10. Print the list after modifying one of the companies
it_companies[2] = 'Mojang'
print(f"IT companies: {it_companies}")
print("-----------------------------------")

# Exercise 11
# 11. Add an IT company to it_companies
it_companies.append('Lenovo')
print(f"IT companies: {it_companies}")
print("-----------------------------------")

# Exercise 12
# 12. Insert an IT company in the middle of the companies list
mid_len = len(it_companies) // 2 - 1
it_companies.insert(mid_len, 'Toshiba')
print("-----------------------------------")

# Exercise 13
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[-1] = it_companies[-1].upper()
print(f"IT companies: {it_companies}")
print("-----------------------------------")

# Exercise 14
# 14. Join the it_companies with a string '#;  '
joined = '#;  '.join(it_companies) + "#;"
print(f"Joined companies with '#;': {joined}")
print("-----------------------------------")

# Exercise 15
# 15. Check if a certain company exists in the it_companies list.
if "Mojang" in it_companies:
    print("Mojang exist in IT companies")
else:
    pass
print("-----------------------------------")

# Exercise 16
# 16. Sort the list using sort() method
it_companies.sort()
print(f"Sorted IT companies: {it_companies}")
print("-----------------------------------")

# Exercise 17
# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(f"Reversed IT companies: {it_companies}")
print("-----------------------------------")

# Exercise 18
# 18. Slice out the first 3 companies from the list
slice = it_companies[:3]
print(f"Sliced the first 3 IT companies: {slice}")
print("-----------------------------------")

# Exercise 19
# 19. Slice out the last 3 companies from the list
slc = it_companies[-3:]
print(f"Sliced the last 3 IT companies: {slc}")
print("-----------------------------------")

# Exercise 20
# 20. Slice out the middle IT company or companies from the list
mid_len = len(it_companies) // 2 - 1
print(f"Sliced middle of IT company: {it_companies[mid_len]}")
print("-----------------------------------")

# Exercise 21
# 21. Remove the first IT company from the list
first = it_companies[0]
it_companies.remove(first)

# Exercise 22
# 22. Remove the middle IT company or companies from the list
mid_len = len(it_companies) // 2 - 1
mid = it_companies[mid_len]
it_companies.remove(mid)
print("-----------------------------------")

# Exercise 23
# 23. Remove the last IT company from the list
last = it_companies[-1]
it_companies.remove(last)

# Exercise 24
# 24. Remove all IT companies from the list
it_companies.clear()

# Exercise 25
# 25. Destroy the IT companies list
del it_companies

# Exercise 26
# 26. Join the following lists:
front_end = [ 'HTML', 'CSS', 'JS', 'React', 'Redux' ]
back_end = [ 'Node','Express', 'MongoDB' ]
join = front_end + back_end
print(join)
print("-----------------------------------")

# Exercise 27
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = join.copy()
redux = full_stack.index('Redux')
print(redux)
full_stack.insert(redux + 1, "Python")
full_stack.insert(redux + 2, "SQL")
print(full_stack)
print("===================================")

## Exercise: level 2
## 1. The following is a list of 10 students ages:
ages = [ 19, 22, 19, 24, 20, 25, 26, 24, 25, 24 ]

# - Sort the list and find the min and max age
ages.sort()
min = ages[0]
max = ages[-1]

# - Add the min age and the max age again to the list
ages.append(min)
ages.append(max)
ages.sort()
print(ages)
print("-----------------------------------")

# - Find the median age (one middle item or two middle items divided by two)
mid_len = len(ages) // 2 - 1
mid = ages[mid_len]
if len(ages) % 2 == 0:
    mid_2_id = mid_len + 1
    mid_2 = ages[mid_2_id]
    if mid == mid_2:
        print(f"The median of ages is: {mid}")
    else:
        median = (mid + mid_2) / 2
        print(f"The median of ages is: {median}")
else:
    median = mid / 2
    print(f"The median of ages is: {median}")
print("-----------------------------------")

# - Find the average age (sum of all items divided by their number )
av = sum(ages) / len(ages)
print(f"The average of the ages is: {av:.0f}")
print("-----------------------------------")

# - Find the range of the ages (max minus min)
print(f"The range of ages is: {max - min}")
print("-----------------------------------")

# - Compare the value of (min - average) and (max - average), use abs() method
min_abs = abs(min - av)
max_abs = abs(max - av)
if min_abs <= max_abs:
    print("Minimal is bigger from average")
else:
    print("Maximal is bigger from average")
print("-----------------------------------")

# 1. Find the middle country(ies) in the countries list
countries = [ 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe',
]
mid_len = len(countries) // 2 - 1
mid = countries[mid_len]
print(len(countries))
print(f"The middle country is: {mid}")
print("-----------------------------------")

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
mid_len = len(countries) // 2 - 1
if len(ages) % 2 == 0:
    mid = mid_len
    first = countries[:mid]
    second = countries[mid:]
else:
    mid = mid_len + 1
    first = countries[:mid]
    second = countries[mid:]

# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic = countries[3]
cn, ru, us, *scandic = countries
print(f"The scandic countries: {scandic}")
print("-----------------------------------")
