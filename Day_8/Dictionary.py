# Day 8: Sets - 30 Days of python programming
# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'krupp'
dog['color'] = 'black'
dog['breed'] = 'Sheperd'
dog['legs'] = 4
dog['age'] = 18

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
        'first_name':'Walter',
        'last_name':'White',
        'Gender':'Male',
        'age':50,
        'marital status':True,
        'skills':['Chemistry', 'Money laundering', 'Mathematic'],
        'country':'USA',
        'city':'Albarqueque',
        'address':{
            'House': 308,
            'Street': 'Negra Arroyo Lane',
            'City': 'Albuquerque',
            'State': 'New Mexico',
            'ZipCode': 87104
            }
        }

# 4. Get the length of the student dictionary
student_len = len(student)
print(f"The length of student dictionary is {student_len}")
print("-----------------------------------")

# 5. Get the value of skills and check the data type, it should be a list
student_skills = student.get('skills')
print(f"Student skills with dataype: {type(student_skills)}")
print("-----------------------------------")

# 6. Modify the skills values by adding one or two skills
student_skills.append('Balling')
student_skills.append('Cooking')
print(student_skills)
print("-----------------------------------")

# 7. Get the dictionary keys as a list
print(student.keys())
print("-----------------------------------")

# 8. Get the dictionary values as a list
print(student.values())
print("-----------------------------------")

# 9. Change the dictionary to a list of tuples using items() method
student.items()
print(student)
print("-----------------------------------")

# 10. Delete one of the items in the dictionary
student.pop()
print(student)
print("-----------------------------------")
