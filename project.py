from task_template import TEXTS
import os

"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Václav Jaroš
email: vaclav.jaros93@gmail.com
discord: vaclavjaros1993
"""

user_data = {"bob" : "123","ann" : "pass123","mike" : "password123",
             "liz" : "pass123"}
separator = "=" * 40

while True:
    if user_name := input("ENTER YOUR NAME: "):
        break
    print("EMPTY INPUT. TRY AGAIN....")

while True:   
    if password := input("ENTER YOUR PASSWORD: "):
        break
    print("EMPTY INPUT. TRY AGAIN...")
    
print(separator)

if password == str(user_data.get(user_name)):
    print(f"WELCOME TO THE APP, {user_name.upper()}!")
    print("WE HAVE 3 TEXTS TO BE ANALYZED.")    
    
    print(separator)
    
else:
    os.system("cls")
    print("UNREGISTERED USER, TERMINATING THE PROGRAM..")
    exit()
         
while True:   
    user_choice = input("CHOOSE TEXT NUMBER TO ANALYZE - |1|2|3|: \n")
    print(separator)

    if not int(user_choice.isnumeric()) or int(user_choice) not in range(1,4):
        os.system("cls")
        print("INVALID INPUT. CHOOSE ONLY NUMBERS BETWEEN 1-3")
        exit()
            
    else:
        user_choice = TEXTS[int(user_choice) - 1]
        break

splited_text = user_choice.split()
words = [word.strip(",.?!") for word in splited_text]
numbers_of_length = [len(word) for word in words]
title_case = [word for word in words if word.istitle()]
all_upper = [word for word in words if word.isupper() and word.isalpha()]
all_lower = [word for word in words if word.islower()]
numeric_string = [word for word in words if word.isnumeric()]
numeric_int = [int(number) for number in numeric_string]

print(f"THERE ARE {len(numbers_of_length)} WORDS IN SELECTED TEXT.")
print(f"THERE ARE {len(title_case)} TITLECASE WORDS.")
print(f"THERE ARE {len(all_upper)} UPPERCASE WORDS.")
print(f"THERE ARE {len(all_lower)} LOWERCASE WORDS.")
print(f"THERE ARE {len(numeric_string)} NUMERIC STRINGS.")
print(f"THE SUM OF ALL THE NUMBERS IS {sum(numeric_int)}.")
print(separator)
print("LEN| OCCURENCES| NR.")
print(separator)

star = "*"
space = " "
set_numbers = set(numbers_of_length)
frequency =  []

for each in set_numbers:
    frequency.append(numbers_of_length.count(each))
highest_number = max(frequency)

for num in set_numbers:
    count_of_spaces = highest_number - numbers_of_length.count(num)
    print(f"{num:2d} | {star * numbers_of_length.count(num)} {space * count_of_spaces} | {numbers_of_length.count(num)}")

