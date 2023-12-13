# Day 5: 30 Days of python programming
# Exercise 1: Level 1
# 1. Declare an empty tuple
empty = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('john', 'denis', 'larry')
sisters = ('amy', 'susan', 'hana')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4. How many siblings do you have?
print(f"I have {len(siblings)} siblings")
print("-----------------------------------")

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
lis_siblings = list(siblings)
lis_siblings.append('jason')
lis_siblings.append('lucia')
family_members = tuple(lis_siblings)
print(family_members)
print("-----------------------------------")

## Exercises: Level 2
# 1. Unpack siblings and parents from family_members
john, denis, larry, amy, susan, hana, *parents = family_members

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter', 'yoghurt')
food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list.
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid_len = len(food_stuff_lt) // 2 - 1
mid = food_stuff_lt[mid_len]
if len(food_stuff_lt) % 2 == 0:
    mid_2_id = mid_len + 1
    mid_2 = food_stuff_lt[mid_2_id]
    print(f"The middle items is: {mid} and {mid_2}")
else:
    print(f"The middle item is: {mid}")
print("-----------------------------------")

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last = food_stuff_lt[:-3]

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
# - Check if 'Estonia' is a nordic country
# - Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
estonia = 'Estonia'
iceland = 'Iceland'
if estonia in nordic_countries:
    print(f"{estonia} is a Nordic country")
else:
    print(f"{estonia} is not nordic country")
print("-----------------------------------")

if iceland in nordic_countries:
    print(f"{iceland} is a Nordic country")
else:
    print(f"{iceland} is not nordic country")
print("-----------------------------------")
