# Day 11: Modules - 30 Days of python programming
import randomcolor
import random
import string

# Exercise: Level 1
# 1. Write a function which generates a six digit/character random_user_id. 
def random_user_id():
    N = 6
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
    return res

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    try:
        N, N2 = input("Enter the length and amount of the random user id: ").split()
        N = int(N)
        N2 = int(N2)

        for _ in range(N2):
            user_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
            print(user_id)

    except ValueError as e:
        print(f"{e}\nInvalid input. Please enter valid number for length and amount.")

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    color = [random.randint(0, 255) for _ in range(3)]
    rgb = tuple(color)
    return rgb

## Exercise: Level 2
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
# - Are they out of mind putting the "Hackerrank" question level in this beginner exercise :skull:
# - It's not easy as generating rgb color bruv
# - So anyway i'm gonna cheat with randomcolor module :trollface:
def list_of_hexa_colors():
    color = randomcolor.RandomColor().generate()
    return color

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
# - let's just add 10 cuz why would you need that much rgb color?
def list_of_rgb_colors():
    n = random.randint(1, 10)
    color = [random.randint(0, 255) for _ in range(3)]
    rgb_array = [color for _ in range(n)]

    return rgb_array

### Exercise: Level 3
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    shuffled = random.shuffle(lst)
    return shuffled

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def array_random():
    length = 7
    random_array = [random.randint(0, 9) for _ in range(length)]
    unique_set = set(random_array)

    while len(unique_set) < length:
        unique_set.add(random.randint(0, 9))
    unique_list = list(unique_set)

    return unique_list
