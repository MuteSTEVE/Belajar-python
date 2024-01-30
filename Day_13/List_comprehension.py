# Day 13: List comprehension - 30 Days of python programming
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/13_Day_List_comprehension/13_list_comprehension.md
# Exercise: Day 13
# 1. Filter only negative and zero in the list using list comprehension
lst = []
lst = [i for i in lst if i <= 0]

# 2. Flatten the following list of lists of lists to a one dimensional list:
# output example
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# I'm still not understand the concept of higher order function yet to create a sophisticated recursion, whatever this is not an interview question anyway
lst =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
def flatten(lst):
    flatten_list = []
    for i in lst:
        for j in i:
            flatten_list.extend(j)
    return flatten_list

# 3. Using list comprehension create the following list of tuples:
# [(0, 0, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
exp = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

# 4. Flatten the following list to a new list:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
def CountryCity(countries):
    countries_flat = []
    for i in countries:
        for j in i:
            countries_flat.extend(j)
    for i in range(len(countries_flat)):
        countries_flat[i] = countries_flat[i].upper()

    country = countries_flat[::2]
    alias = [i[:3] for i in country]
    city = countries_flat[1::2]

    result = [[country[i], alias[i], city[i]] for i in range(len(country))]
    return result

# 5. Change the following list to a list of dictionaries:
# countries = [[('finland', 'helsinki')], [('sweden', 'stockholm')], [('norway', 'oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
countries = [[('finland', 'helsinki')], [('sweden', 'stockholm')], [('norway', 'oslo')]]
def DictCountry(countries):
    countries_flat = []
    for i in countries:
        for j in i:
            countries_flat.extend(j)
    for i in range(len(countries_flat)):
        countries_flat[i] = countries_flat[i].upper()

    country = countries_flat[::2]
    city = countries_flat[1::2]

    result = [{'country': country[i], 'city': city[i]} for i in range(len(country))]
    return result

# 6. Change the following list of lists to a list of concatenated strings:
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
def FullName(names):
    names_flat = []
    for i in names:
        for j in i:
            names_flat.extend(j)

    first = names_flat[::2]
    last = names_flat[1::2]

    full = [[first[i] + " " + last[i]] for i in range(len(first))]
    full_name = []
    for i in full:
        full_name.extend(i)
    return full_name

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
# - I can't do math bro
