# Day 4: 30 Days of python programming

# Exercise 1
# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
text_join = ['Thirty', 'Days', 'Of', 'Python']
tdop = ' '.join(text_join)
print(tdop)
print("-----------------------------------")

# Exercise 2
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
text_join = ['Coding', 'For' , 'All']
text = ' '.join(text_join)
print(text)
print("-----------------------------------")

# Exercise 3
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Exercise 4
# 4. Print the variable company using print().
print(company)
print("-----------------------------------")

# Exercise 5
# 5. Print the length of the company string using len() method and print().
print(f"The length of the 'company' is is: {len(company)}")
print("-----------------------------------")

# Exercise 6
# 6. Change all the characters to uppercase letters using upper() method.
text_case = 'thirty days of python'
text_case_up = text_case.swapcase()
print(text_case_up)
print("-----------------------------------")

# Exercise 7
# 7. Change all the characters to lowercase letters using lower() method.
text_case_low = text_case_up.swapcase()
print(text_case_low)
print("-----------------------------------")

# Exercise 8
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
text = "Coding For All"
capitalize = text.capitalize()
title = text.title() 
swapcase = text.swapcase()
print(f"capitalize(): {capitalize}")
print(f"title(): {title}")
print(f"swapcase(): {swapcase}")
print("-----------------------------------")

# Exercise 9
# 9. Cut(slice) out the first word of Coding For All string.
text = "Coding For All"
print(f"{text}[:6] : {text[:6]}")
print("-----------------------------------")

# Exercise 10
# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
text = "Coding For All"
count = text.count('Coding')
find = text.find('Coding')
index = text.index('Coding')
print(f"There are total {count} 'Coding' contained in {text}")
print(f"Found 'Coding' in {text} first seen in index {find}")
print(f"The position of 'Coding' in {text} first seen in index {index}")
print("-----------------------------------")

# Exercise 11
# 11. Replace the word coding in the string 'Coding For All' to Python.
replace_coding = text.replace('Coding', 'Python')
print(f"Replacing the word to '{replace_coding}'")
print("-----------------------------------")

# Exercise 12
# 12. Change Python for Everyone to Python for All using the replace_coding method or other methods.
text = "Python for Everyone"
replace_everyone = text.replace('Everyone', 'All')
print(f"Replacing the word to '{replace_everyone}'")
print("-----------------------------------")

# Exercise 13
# 13. Split the string 'Coding For All' using space as the separator (split()) .
text = "Coding For All"
split = text.split(', ')
print(split)
print("-----------------------------------")

# Exercise 14
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
split = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(split.split(', '))
print("-----------------------------------")

# Exercise 15
# 15. What is the character at index 0 in the string Coding For All.
text = "Coding For All"
print(f"The first index of {text}[0] is: {text[0]}")
print("-----------------------------------")

# Exercise 16
# 16. What is the last index of the string Coding For All.
text = "Coding For All"
print(f"The last index of {text}[-1] is: {text[-1]}")
print("-----------------------------------")

# Exercise 17
# 17. What character is at index 10 in "Coding For All" string.
text = "Coding For All"
print(f"The last index of {text}[10] is: {text[10]}")
print("-----------------------------------")

# Exercise 18
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
text = "Python for Everyone"
text_split = text.split()
ac_0 = text_split[0][0]
ac_1 = text_split[1][0]
ac_2 = text_split[2][0]
acronym = [ac_0, ac_1, ac_2]
acronym_join = ' '.join(acronym)
print(f"{text} acronym is: '{acronym_join}'")
print("-----------------------------------")

# Exercise 19
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
text = "Coding For All"
text_split = text.split()
ac_0 = text_split[0][0]
ac_1 = text_split[1][0]
ac_2 = text_split[2][0]
acronym = [ac_0, ac_1, ac_2]
acronym_join = ' '.join(acronym)
print(f"{text} acronym is: '{acronym_join}'")
print("-----------------------------------")

# Exercise 20
# 20. Use index to determine the position of the first occurrence of C in Coding For All.
text = "Coding For All"
index = text.index('C')
print(f"The position of 'Coding' in {text} first seen in index {index}")
print("-----------------------------------")

# Exercise 21
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
text = "Coding For All"
index = text.index('F')
print(f"The position of 'Coding' in {text} first seen in index {index}")
print("-----------------------------------")

# Exercise 22
# 22. Use index to determine the position of the first occurrence of F in Coding For All.
text = "Coding For All People"
rfind = text.rfind('F')
print(f"Found 'Coding' in {text} first seen in index {rfind}")
print("-----------------------------------")

# Exercise 23
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text = "You cannot end a sentence with because because because is a conjunction"
because = "because"
find = text.find(because)
index = text.index(because)
print(f"Found {because} in first seen in index {find}")
print(f"The position of {because} in first seen in index {index}")
print("-----------------------------------")

# Exercise 24
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text = "You cannot end a sentence with because because because is a conjunction"
because = "because"
find = text.find(because)
rindex = text.rindex(because)
print(f"Found {because} in first seen in index {find}")
print(f"The position of {because} in first seen in index {rindex}")
print("-----------------------------------")

# Exercise 25
# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text = "You cannot end a sentence with because because because is a conjunction"
text_slice = text[31:54]
print(text_slice)
print("-----------------------------------")

# Exercise 26
# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text = "You cannot end a sentence with because because because is a conjunction"
because = "because"
find = text.find(because)
print(f"Found {because} in first seen in index {find}")
print("-----------------------------------")

# Exercise 27
# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text = "You cannot end a sentence with because because because is a conjunction"
text_slice = text[31:54]
print(text_slice)
print("-----------------------------------")

# Exercise 28
# 28. Does ''Coding For All' start with a substring Coding?
text = "Coding For All"
coding = 'Coding'
startwith = text.count(coding)

if text.startswith('Coding'):
    print(f"{text} start with '{coding}'")
else:
    print(f"{text} doesn't start with '{coding}'")
print("-----------------------------------")

# Exercise 30
# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
text = "   Coding For All      "
tabs = text.expandtabs()
print(tabs)
print("-----------------------------------")

# Exercise 33
# 33. Use the new line escape sequence to separate the following sentences. 
print("I am enjoying this challenge.\nI just wonder what is next.")
print("-----------------------------------")

# Exercise 34
# 34. Use a tab escape sequence to write the following lines. 
name = "Satrio"
age = 18
country = "Indonesia"
city = "Jakarta"
print(f"Name\tAge\tCountry\tCity\n{name}\t{age}\t{country}\t{city}")
print("-----------------------------------")

# Exercise 35
# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.2f} meters square.")
print("-----------------------------------")

# Exercise 36
# 36. Make the following using string formatting methods:
n1, n2 = 8, 6
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")
print(f"{n1} / {n2} = {n1 / n2:.2f}")
print(f"{n1} % {n2} = {n1 % n2}")
print(f"{n1} // {n2} = {n1 // n2}")
print(f"{n1} ** {n2} = {n1 ** n2}")
print("-----------------------------------")
