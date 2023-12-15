# Day 5 Sets: 30 Days of python programming
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# 1. Find the length of the set it_companies
it_companies_len = len(it_companies)

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update({'Mojang', 'Konami', 'Nintendo'})

# 4. Remove one of the companies from the set it_companies
it_companies.pop()

# 5. What is the difference between remove and discard
# - remove() will check if the desired item is exist or not, if it's not then it will raised an error, unlike discard() if the desired item doesn't exist it will not raised any error

## Exercises: Level 2
# 1. Join A and B
uni = A.union(B)

# 2. Find A intersection B
intersection = A.intersection(B)

# 3. Is A subset of B
if A.issubset(B) == 1:
    print("A is subset of B")
else:
    print("A is not subset of B")
print("-----------------------------------")

# 4. Are A and B disjoint sets
if A.isdisjoint(B) == 1:
    print("A and be are disjoint sets")
else:
    print("A and be are not disjoint sets")
print("-----------------------------------")

# 5. Join A with B and B with A
union_ab = A.union(B)
union_ba = B.union(A)

# 6. What is the symmetric difference between A and B
sym = A.symmetric_difference(B)
print(f"The symmetric difference between A and B are: {sym}")
print("-----------------------------------")

# 7. Delete the sets completely
del it_companies
del A
del B

### Exercises: Level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_lt = list(age)
if len(age_lt) > len(age):
    print("Age list has longer length than age tuple")
elif len(age_lt) < len(age):
    print("Age tuple has longer length than age list")
else:
    print("Both age tuple and list are the same length")
print("-----------------------------------")

# 2. Explain the difference between the following data types: string, list, tuple and set
print("""
- String can only containt one item inside a surrounding single/double quotes, string are mutable means the content inside can be changed/modified
- List are collection of multiple strings inside of square brackets, the content of list are ordered so it can be sorted accordingly, list are mutable means all the string inside can be changed/modified
- Tuple are collection of multiple strings inside of parenteheses, the content of tuple are ordered, but unlike list tuple are immutable means all the string inside can't be chnaged/modified
- Set are collection of multiple strings inside of curly brackets, it's the same things as list. It's mutable means the content inside can be changed but unlike string, the content of set are unordered means it can't be sorted accordingly
      """)

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
txt = "I am a teacher and I love to inspire and teach people"
unique = txt.split()
print(f"It consist {len(unique)} of uniqe words")
